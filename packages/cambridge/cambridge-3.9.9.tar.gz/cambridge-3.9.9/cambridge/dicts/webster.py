import requests
import threading
import sys
from lxml import etree

from ..console import c_print
from ..utils import get_request_url, decode_url, OP, DICT
from ..log import logger
from ..dicts import dict
from ..errors import NoResultError
from .. import color as w_col

WEBSTER_BASE_URL = "https://www.merriam-webster.com"
WEBSTER_DICT_BASE_URL = WEBSTER_BASE_URL + "/dictionary/"
WEBSTER_WORD_OF_THE_DAY_URL = WEBSTER_BASE_URL + "/word-of-the-day"

sub_text = ""
res_word = ""
word_entries = [] # A page may have multiple word entries, e.g. "give away", "giveaway"
word_forms = []   # A word may have multiple word forms, e.g. "ran", "running", "run", "flies"
word_types = []   # A word's word types, e.g. "preposition", "adjective"


def search_webster(con, cur, input_word, is_fresh=False, no_suggestions=False):
    """
    Entry point for searching a word in Webster.
    It first checks the cache, if the word has been cached,
    uses it and prints it; if not, go fetch the web.
    If the word is found, prints it to the terminal and caches it concurrently.
    if not found, prints word suggestions and exit.
    """

    req_url = get_request_url(WEBSTER_DICT_BASE_URL, input_word, DICT.MERRIAM_WEBSTER.name)

    if not is_fresh:
        cached = dict.cache_run(con, cur, input_word, req_url, DICT.MERRIAM_WEBSTER.name)
        if not cached:
            fresh_run(con, cur, req_url, input_word, no_suggestions)
    else:
        fresh_run(con, cur, req_url, input_word, no_suggestions)


def fetch_webster(request_url, input_word):
    """Get response url and response text for future parsing."""

    with requests.Session() as session:
        session.trust_env = False
        res = dict.fetch(request_url, session)

        res_url = res.url
        res_text = res.text
        status = res.status_code

        if status == 200:
            logger.debug(f'{OP.FOUND.name} "{input_word}" in {DICT.MERRIAM_WEBSTER.name} at {res_url}')
            return True, (res_url, res_text)

        # By default Requests will perform location redirection for all verbs except HEAD.
        # https://requests.readthedocs.io/en/latest/user/quickstart/#redirection-and-history
        # You don't need to deal with redirection yourself.
        # if status == 301:
        #     loc = res.headers["location"]
        #     new_url = WEBSTER_BASE_URL + loc
        #     new_res = dict.fetch(new_url, session)

        elif status == 404:
            logger.debug(f'{OP.NOT_FOUND.name} "{input_word}" in {DICT.MERRIAM_WEBSTER.name}')
            return False, (res_url, res_text)

        else:
            logger.error(f'Something went wrong when fetching {request_url} with STATUS: {status}')
            sys.exit()


def fresh_run(con, cur, req_url, input_word, no_suggestions=False):
    """Print the result without cache."""

    result = fetch_webster(req_url, input_word)
    found = result[0]
    res_url, res_text = result[1]
    nodes = parse_dict(res_text, found, res_url, True)

    if found:
        if res_word:
            parse_thread = threading.Thread(
                target=parse_and_print, args=(nodes, res_url, True)
            )
            parse_thread.start()

            # sqlite must be in the main thread.
            # sqlite3.ProgrammingError:
            # SQLite objects created in a thread can only be used in that same thread.
            # The object was created in thread id 140704708548544 and this is thread id 123145383600128.
            dict.save(con, cur, input_word, res_word, res_url, sub_text)
    else:
        if no_suggestions:
            sys.exit(-1)
        else:
            logger.debug(f"{OP.PRINTING.name} the parsed result of {res_url}")
            suggestions = []
            for node in nodes:
                if node.tag != "h1":
                    for word in node.itertext():
                        w = word.strip()
                        if w.startswith("The"):
                            continue
                        else:
                            sug = w.strip()
                            suggestions.append(sug)

            dict.print_spellcheck(con, cur, input_word, suggestions, DICT.MERRIAM_WEBSTER.name)


def get_wod():
    result = fetch_webster(WEBSTER_WORD_OF_THE_DAY_URL, "")
    found = result[0]
    if found:
        res_url, res_text = result[1]
        parse_and_print_wod(res_url, res_text)


def parse_redirect(nodes, res_url):
    input_word = decode_url(res_url).split("/")[-1]
    print("No exact result found.")
    c_print(f"The following entries include the term #[#b22222 bold]{input_word}#[/#b22222 bold].")

    for node in nodes:
        try:
            attr = node.attrib["id"]
        except KeyError:
            attr = node.attrib["class"]

        if "row entry-header" in attr:
            print()
            row_entry_header(node, True)
            continue

        if "-entry" in attr:
            print()
            for n in node.iterchildren():
                if n.tag == "div" and n.attrib["class"] == "vg":
                    for child in n.iterchildren():
                        if child.tag == "p":
                            x = list(child.itertext())
                            print("".join(x).strip())
            continue

    c_print(f'\n#[#757575]You can add "camb -w" before one above entry to get its full definition from the {DICT.MERRIAM_WEBSTER.name} dictionary')


def parse_dict(res_text, found, res_url, is_fresh):
    """Parse the dict section of the page for the word."""

    logger.debug(f"{OP.PARSING.name} {res_url}")

    parser = etree.HTMLParser(remove_comments=True)
    tree = etree.HTML(res_text, parser)

    if found:
        sub_tree = tree.xpath('//*[@id="left-content"]')[0]

        s = """
        //*[@id="left-content"]/div[contains(@id, "-entry")] |
        //*[@id="left-content"]/div[@id="phrases"] |
        //*[@id="left-content"]/div[@id="synonyms"] |
        //*[@id="left-content"]/div[@id="examples"]/div[@class="content-section-body"]/div[contains(@class,"on-web-container")]/div[contains(@class,"on-web")] |
        //*[@id="left-content"]/div[@id="related-phrases"] |
        //*[@id="left-content"]/div[@id="nearby-entries"]
        """

        nodes = sub_tree.xpath(s)

        if is_fresh:
            global sub_text
            sub_text = etree.tostring(sub_tree).decode('utf-8')

        if len(nodes) == 0:
            print(NoResultError(DICT.MERRIAM_WEBSTER.name))
            sys.exit()

        result = sub_tree.xpath('//*[@id="left-content"]/div[contains(@id, "-entry-1")]/div[1]/div/div[1]/h1/text()') \
              or sub_tree.xpath('//*[@id="left-content"]/div[contains(@id, "-entry-1")]/div[1]/div/div/h1/span/text()')

        if len(result) != 0:
            global res_word
            res_word = result[0]
        else:
            redirect_s = """
            //*[@id="left-content"]/div[contains(@id, "-entry")] |
            //*[@id="left-content"]/div[contains(@class, "row entry-header")]
            """
            nodes = sub_tree.xpath(redirect_s)
            parse_redirect(nodes, res_url)

        ## NOTE: [only for debug]
        # for node in nodes:
        #     try:
        #         print("id:    ", node.attrib["id"])
        #     except KeyError:
        #         print("class: ", node.attrib["class"])

        # sys.exit()

    else:
        result = tree.xpath('//div[@class="widget spelling-suggestion"]')
        if len(result) != 0:
            nodes = result[0]
        else:
            print(NoResultError(DICT.MERRIAM_WEBSTER.name))
            sys.exit()
    return nodes


###########################################
# parse and print nearby entries
###########################################

def nearby_entries(node):
    print()

    for elm in node.iterdescendants():
        try:
            has_title = (elm.tag == "h2")
            has_word = (elm.tag == "span") and (elm.attrib["class"] == "b-link hw-text fw-bold")
            has_nearby = (elm.tag == "a") and (elm.attrib["class"] == "b-link")
            has_em = (elm.tag == "em")
        except KeyError:
            continue
        else:
            if has_title:
                c_print(f"#[bold {w_col.nearby_title}]{elm.text}", end="")
                continue

            if has_em:
                word = "".join(list(elm.itertext()))
                c_print(f"#[bold {w_col.nearby_em}]{word}", end="\n")
                continue

            if has_word:
                c_print(f"#[{w_col.nearby_word}]{elm.text}", end="\n")
                continue

            if has_nearby:
                c_print(f"#[{w_col.nearby_item}]{elm.text}", end="\n")
                continue


###########################################
# parse and print synonyms
###########################################

def synonyms(node):
    print()

    for elm in node.iterdescendants():
        try:
            has_title = (elm.tag == "h2") # "Synonyms"
            has_label = (elm.tag == "p") and (elm.attrib["class"] == "function-label") # "Noun"
            has_syn = (elm.tag == "ul") # synonym list
        except KeyError:
            continue
        else:
            if has_title:
                c_print(f"#[bold {w_col.syn_title}]{elm.text}", end=" ")

            if has_label:
                c_print(f"\n#[{w_col.syn_label}]{elm.text}")

            if has_syn:
                children = elm.getchildren()
                total_num = len(children)

                for index, child in enumerate(children):
                    syn = "".join(list(child.itertext())).strip()
                    if index != (total_num - 1):
                        c_print(f"#[{w_col.syn_item}]{syn},", end=" ")
                    else:
                        c_print(f"#[{w_col.syn_item}]{syn}", end=" ")


###########################################
# parse and print examples
###########################################

# NOTE:
# Wester scrapes the web for examples in the way that it only finds the exact match of the word.
# If the word is a verb, only gets the word without tenses; if the word is a noun, only its single form.
def examples(node):
    time = 0

    for elm in node.iterdescendants():
        try:
            is_title = ("ex-header function-label" in elm.attrib["class"]) # Recent Examples on the Web
            has_aq = (elm.attrib["class"] == "t has-aq")
        except KeyError:
            continue
        else:
            if is_title:
                c_print(f"\n#[{w_col.eg_title} bold]{elm.text}", end="")
            if has_aq:
                texts = list(elm.itertext())

                for index, t in enumerate(texts):
                    if time in [0, 1, 8, 9, 16, 17, 24, 25]:
                        if index == 0:
                            c_print(f"\n#[{w_col.accessory}]|", end="")
                            c_print(f"#[{w_col.eg_sentence}]{t}", end="")
                        else:
                            hit = False
                            global word_entries, word_forms
                            words = set(word_entries)
                            forms = set(word_forms)
                            text = t.strip().lower()
                            for w in words:
                                if "preposition" in word_types or "adverb" in word_types or "conjuction" in word_types and ("noun" in word_types and text[-1] !="s"):
                                    if w == text:
                                        hit = True
                                        break
                                else:
                                    if w in text and len(text) < 20:
                                        hit = True
                                        break
                            for f in forms:
                                if f == text:
                                    hit = True
                                    break

                            if hit:
                                c_print(f"#[{w_col.eg_sentence} bold]{t}", end="")
                            else:
                                c_print(f"#[{w_col.eg_sentence}]{t}", end="")
                    else:
                        continue
                time = time + 1


###########################################
# parse and print phrases
###########################################

def phrases(node):
    print()

    children = node.getchildren()[1]
    for child in children:
        try:
            if child.attrib["class"] == "drp":
                if child.getnext().tag == "span":
                    c_print(f"#[{w_col.ph_item} bold]{child.text}", end = "")
                else:
                    c_print(f"#[{w_col.ph_item} bold]{child.text}", end = "\n")

            if child.attrib["class"] == "vg":
                vg(child)

        except KeyError:
            for i in child.getchildren():
                if i.attrib["class"] == "vl":
                    print_or_badge(i.text)
                else:
                    c_print(f"#[{w_col.ph_item} bold]{i.text}", end = "\n")


##########################################################
# parse and print related phrases (Phrases Containing ...)
##########################################################

def related_phrases(node):
    print()

    children = node.getchildren()

    title = children[1]
    texts = list(title.itertext())
    global word_entries
    words = set(word_entries)

    for t in texts:
        if t.strip():
            if t.lower() in words:
                c_print(f"#[{w_col.rph_em} bold]{t}", end="\n")
            else:
                c_print(f"#[{w_col.rph_title} bold]{t}", end="")

    pr_sec = children[2]
    phrases = [] # li tags, each tag has one phrase
    for i in pr_sec.iterdescendants():
        if i.tag == "li":
            phrases.append(i)

    for phrase in phrases:
        ts = list(phrase.itertext())
        ts = "". join(ts).strip("\n").strip()
        if phrase != phrases[-1]:
            c_print(f"#[{w_col.rph_item}]{ts},", end=" ")
        else:
            c_print(f"#[{w_col.rph_item}]{ts}", end="")


###########################################
# parse and print dictionary-entry-[number]
###########################################

# --- parse class "vg" --- #
def get_word_cases(node):
    l_words = []
    u_words = []
    for i in node.iterdescendants():
        attr = i.get("class")
        if attr is not None:
            if "lowercase" in attr:
                l_words.append(i.text)
            if "uppercase" in attr:
                u_words.append(i.text)
    return l_words, u_words

def dtText(node, ancestor_attr):
    texts = list(node.itertext())

    l_words = get_word_cases(node)[0]
    u_words = get_word_cases(node)[1]

    if node.getprevious() is not None and node.getprevious().get("class") == "sub-content-thread":
        format_basedon_ancestor(ancestor_attr, prefix="\n")

    for index, text in enumerate(texts):
        if text == " " and index == 0:
            continue
        if text == ": ":
            print_meaning_content(text, end="")
        elif text == " see also ":
            print_meaning_keyword(text.strip())
        elif text == " see " or text == " compare ":
            print_meaning_keyword("->" + text.strip())
        elif u_words and text in u_words:
            text_new = text.upper()
            print_meaning_content(text_new, end="")
        elif l_words and text in l_words:
            text_new = (" " + text)
            print_meaning_content(text_new, end="")
        else:
            print_meaning_content(text, end="")

    print("", end = " ")


def print_mw(text, has_tail, tag):
    if tag == "hl":
        if has_tail is True:
            c_print(f"#[{w_col.meaning_sentence} bold]{text}", end = "")
        else:
            c_print(f"#[{w_col.meaning_sentence} bold]{text}", end = " ")
    if tag == "normal":
        if has_tail is True:
            c_print(f"#[{w_col.meaning_sentence}]{text}", end = "")
        else:
            c_print(f"#[{w_col.meaning_sentence}]{text}", end = " ")


def ex_sent(node, ancestor_attr, num_label_count=1):
    if ancestor_attr:
        format_basedon_ancestor(ancestor_attr, prefix="\n")
    else:
        print("")

    if num_label_count == 2:
        print(" ", end="")

    c_print(f"#[{w_col.accessory}]|", end="")

    hl_words = []
    ems = []
    for i in node.iterdescendants():
        attr = i.get("class")
        if attr is not None:
            if i.tag == "em" and "mw" in attr:
                ems.append(i.text)
                continue
            if i.tag == "span" and "mw" in attr:
                hl_words.append(i.text)
                continue

    texts = list(node.itertext())
    count = len(texts)

    for index, t in enumerate(texts):
        text = t.strip("\n").strip()
        if text:
            if t in hl_words:
                hl_has_tail = ((index != (count - 1)) and (texts[index + 1].strip("\n").strip()) and (not texts[index + 1].strip("\n").strip()[0].isalnum()))
                print_mw(text, hl_has_tail, "hl")
            elif t in ems:
                if index != 0 and texts[index - 1].endswith(" "):
                    print("", end = " ")
                c_print(f"#[{w_col.meaning_sentence} bold]{text}", end = "")
                if index != (count - 1) and texts[index + 1].startswith(" "):
                    print("", end = " ")
            else:
                normal_has_tail = (index != (count - 1) and (texts[index + 1] in ems))
                print_mw(text, normal_has_tail, "normal")


def sub_content_thread(node, ancestor_attr, num_label_count=1):
    children = node.getchildren()
    for child in children:
        attr = child.attrib["class"]

        if ("ex-sent" in attr) and ("aq has-aq" not in attr):
            ex_sent(child, ancestor_attr, num_label_count)
            continue

        if "vis" in attr:
            elms = child.getchildren()
            for e in elms:
                elm = e.getchildren()[0]
                elm_attr = elm.attrib["class"]
                if ("ex-sent" in elm_attr) and ("aq has-aq" not in elm_attr):
                    ex_sent(elm, ancestor_attr, num_label_count)
            continue


def extra(node, ancestor_attr):
    texts = list(node.itertext())

    l_words = get_word_cases(node)[0]
    u_words = get_word_cases(node)[1]

    for text in texts:
        text_new = text.strip("\n").strip()
        if text_new:
            if text_new == "called also" or text_new == "compare":
                print_meaning_badge("->" + text_new)
            elif u_words and text in u_words:
                text_new = text_new.upper()
                print_meaning_content(text_new, end="")
            elif l_words and text in l_words:
                text_new = (" " + text_new)
                print_meaning_content(text_new, end="")
            elif text_new == ",":
                print_meaning_content(text_new, end=" ")
            else:
                print_meaning_content(text_new, end="")

    print("", end = " ")


def unText_simple(node, ancestor_attr, num_label_count=1, has_badge=True):
    text = "".join(list(node.itertext())).strip()

    if not has_badge:
        print()
        if num_label_count == 2:
            print(" ", end="")
        format_basedon_ancestor(ancestor_attr, prefix="")

    node_pre = node.getprevious()
    node_pre_attr = node_pre.get("class")

    if "mdash" in node_pre_attr:
        print_meaning_arrow("->" + text)
    else:
        print_meaning_badge(text)


### sense(node, "sense has-sn", "sb-0 sb-entry, "sb has-num has-let ms-lg-4 ms-3 w-100", 1)
def sense(node, attr, parent_attr, ancestor_attr, num_label_count=1):
    children = node.getchildren()

    # meaning without any sign
    if attr == "sense  no-subnum":
        sense_content = children[0] # class "sense-content w-100"

    # meaning with "1" + "a"
    elif attr == "sense has-sn has-num":
        sn = children[0].getchildren()[0].text

        node_prev = node.getprevious()
        if "has-subnum" in ancestor_attr and node_prev is None and "sb-0" in parent_attr:
            c_print(f"#[bold {w_col.meaning_letter}]{sn}", end = " ")
        elif "has-subnum" in ancestor_attr and (node_prev is not None or parent_attr != "pseq no-subnum"):
            if num_label_count == 2:
                print(" ", end="")
            c_print(f"  #[bold {w_col.meaning_letter}]{sn}", end = " ")
        else:
            c_print(f"#[bold {w_col.meaning_letter}]{sn}", end = " ")

        sense_content = children[1] # class "sense-content w-100"

    # meaing with only "b" or "1" + "a" + "(1)", or "1" + "a"
    elif attr == "sense has-sn" or attr == "sen has-sn":
        sn = children[0].getchildren()[0].text

        if "has-subnum" in ancestor_attr and "sb-0" in parent_attr:
            c_print(f"#[bold {w_col.meaning_letter}]{sn}", end = " ")
        else:
            if num_label_count == 2:
                    print(" ", end="")

            if "letter-only" in ancestor_attr:
                if "sb-0" not in parent_attr:
                    print("  ", end="")
                c_print(f"#[bold {w_col.meaning_letter}]{sn}", end = " ")
            else:
                c_print(f"  #[bold {w_col.meaning_letter}]{sn}", end = " ")

        sense_content = children[1] # class "sense-content w-100"

    # meaning with only (2)
    elif attr == "sense has-num-only has-subnum-only":
        if num_label_count == 2:
            print(" ", end="")
        if "letter-only" in ancestor_attr:
            if children[0].attrib["class"] == "sn":
                print("    ", end = "")
            else:
                print("  ", end="")
        else:
            print("    ", end = "")
        sense_content = children[1] # class "sense-content w-100"

    # meaning with only number
    elif attr == "sense has-sn has-num-only":
        sense_content = children[1] # class "sense-content w-100"

    else:
        sense_content = children[1]

    # "sense-content w-100"
    tags(sense_content, attr, num_label_count)


def sb_entry(node, parent_attr, num_label_count=1):
    child = node.getchildren()[0]
    attr = node.attrib["class"]         # "sb-0 sb-entry"
    child_attr = child.attrib["class"]  # "sense has-sn" or "pseq no-subnum"
    if "pseq" in child_attr:
        elms = child.getchildren()[0].getchildren()
        for e in elms:
            e_attr = e.attrib["class"]  # "sense has-sn"
            sense(e, e_attr, attr, parent_attr, num_label_count)     # e.g. sense(child, "sense has-sn", "sb-0 sb-entry", "....", 1)
    elif "sense" in child_attr and child.tag != "span":
        sense(child, child_attr, attr, parent_attr, num_label_count) # e.g. sense(child, "sense has-sn", "sb-0 sb-entry, "sb has-num has-let ms-lg-4 ms-3 w-100", 1)


def tags(node, ancestor_attr, num_label_count):
    has_badge = True

    for elm in node.iterdescendants():
        elm_attr = elm.get("class")
        if elm_attr is not None:
            if "badge" in elm_attr:
                text = "".join(list(elm.itertext())).strip()
                print_meaning_badge(text)
                continue

            if elm_attr == "et":
                et(elm)
                continue

            if elm_attr == "il ":
                print_meaning_badge(elm.text.strip(), end=" ")
                continue

            if elm_attr == "if":
                print_class_if(elm.text)
                continue

            if elm_attr == "sgram":
                print_class_sgram(elm)
                continue

            if elm_attr == "vl":
                print_meaning_badge(elm.text.strip())
                continue

            if elm_attr == "va":
                print_class_va(elm.text.strip())
                continue

            if elm_attr == "sd":
                parent = elm.getparent()
                parent_attr = parent.get("class")
                parent_prev = parent.getprevious()
                if parent_prev is not None and "hasSdSense" in parent_prev.get("class"):
                    print()
                if parent_attr is not None and parent_attr == "sdsense":
                    format_basedon_ancestor(ancestor_attr, prefix="")

                if num_label_count == 2:
                    print(" ", end="")

                print_meaning_badge(elm.text)

            if elm_attr == "dtText":
                dtText(elm, ancestor_attr) # only meaning text
                continue

            if elm_attr == "sub-content-thread":
                sub_content_thread(elm, ancestor_attr, num_label_count) # example under the meaning
                has_badge = False
                continue

            if elm_attr == "ca":
                extra(elm, ancestor_attr)
                continue

            if elm_attr == "unText":
                unText_simple(elm, ancestor_attr, num_label_count, has_badge)
                continue

    print()


def vg_sseq_entry_item(node):
    """Print one meaning of one entry(noun entry, adjective entry, or verb entry and so forth). e.g. 1: the monetary worth of something."""

    num_label_count = 0
    children = node.getchildren()
    for child in children:
        attr = child.attrib["class"]
        # print number label if any
        if attr == "vg-sseq-entry-item-label":
            c_print(f"#[bold {w_col.meaning_num}]{child.text}", end=" ")
            num_label_count = len(child.text)

        # print meaning content
        if "ms-lg-4 ms-3 w-100" in attr:
            for c in child.iterchildren(): # c:  class="sb-0 sb-entry"
                cc = c.getchildren()[0]    # cc: class="sen has-num-only"
                cc_attr = cc.get("class")
                if cc_attr is not None and cc_attr == "sen has-num-only":
                    tags(cc, cc_attr, num_label_count)

                # print class "sb-0 sb-entry", "sb-1 sb-entry" ...
                sb_entry(c, attr, num_label_count)

def et(node):
    for t in node.itertext():
        print(t.strip("\n"), end= "")

    if node.getnext() is None:
        print()
    else:
        print("", end=" ")

def vg(node):
    """Print one entry(e.g. 1 of 3)'s all meanings. e.g. 1 :the monetary worth of something 2 :a fair return... 3 :..."""

    children = node.getchildren()
    for child in children:
        # print one meaning of one entry
        if "vg-sseq-entry-item" in child.attrib["class"]:
            vg_sseq_entry_item(child)

        # print transitive or intransitive
        if child.attrib["class"] == "vd firstVd" or child.attrib["class"] == "vd":
            e = child.getchildren()[0]
            c_print(f"#[bold]{e.text}")

        # print tags like "informal" and the tags at the same livel with transitives
        if "sls" in child.attrib["class"]:
            e = child.getchildren()[0]
            e_attr = e.get("class")
            if e_attr is not None and "badge" in e_attr:
                print_meaning_badge(e.text)
            else:
                c_print(f"#[bold]{e.text}")


# --- parse class "row entry-header" --- #
def print_word(text):
    c_print(f"#[{w_col.eh_h1_word} bold]{text}", end=" ")


def entry_header_content(node):
    """Print entry header content. e.g. value 1 of 3 noun"""

    for elm in node.iterchildren():
        if elm.tag == "h1" or elm.tag == "p":
            word = "".join(list(elm.itertext()))
            global word_entries
            word_entries.append(word.strip().lower())
            print_word(word)

        if elm.tag == "span":
            num = " ".join(list(elm.itertext()))
            print(num, end=" ")

        if elm.tag == "h2":
            type = " ".join(list(elm.itertext()))
            c_print(f"#[bold {w_col.eh_word_type}]{type}", end="")
            global word_types
            word_types.append(type.strip().lower())
    print()


def entry_attr(node):
    """Print the pronounciation. e.g. val·​ue |ˈval-(ˌ)yü|"""

    for elm in node.iterchildren():
        if "col word-syllables-prons-header-content" in elm.attrib["class"]:
            for i in elm.iterchildren():
                if i.tag == "span" and i.attrib["class"] == "word-syllables-entry":
                    syllables = i.text
                    print(f"{syllables}", end=" ")

                if i.tag == "span" and "prons-entries-list-inline" in i.attrib["class"]:
                    print_pron(i, True)


def row_entry_header(node, is_redirect=False):
    """Print class row entry-header, the parent and caller of entry_header_content() and entry_attr()."""

    for elm in node.iterchildren():
        if elm.attrib["class"] == "col-12":
            for i in elm.iterchildren():
                if "entry-header-content" in i.attrib["class"]:
                    entry_header_content(i)
                if "row entry-attr" in i.attrib["class"]:
                    entry_attr(i)

                if is_redirect:
                    if "hword" == i.attrib["class"]:
                        hword = "".join(list(i.itertext()))
                        c_print(f"#[bold {w_col.eh_h1_word}]{hword}", end=" ")
                    if "fl" == i.attrib["class"]:
                        type = "".join(list(i.itertext()))
                        c_print(f"#[bold {w_col.eh_word_type}]{type}", end="")

# --- parse class "entry-uros" --- #
def entry_uros(node):
    """Print other word forms. e.g. valueless, valuelessness"""

    for elm in node.iterdescendants():
        attr = elm.get("class")
        if attr is not None:
            if elm.tag == "span" and "fw-bold ure" in attr:
                c_print(f"#[bold {w_col.wf}]{elm.text}", end = " ")
                continue

            if elm.tag == "span" and "fw-bold fl" in attr:
                next_sibling = elm.getnext()
                c_print(f"#[{w_col.eh_word_type}]{elm.text}", end = "")
                continue

            if "ins" in attr:
                print("", end="")
                print_class_ins(elm)
                continue

            if "sl badge" in attr:
                text = "".join(list(elm.itertext())).strip()
                print_meaning_badge(text)
                continue

            if "utxt" in attr:
                for i in elm.iterchildren():
                    sub_attr = i.get("class")
                    if sub_attr is not None and sub_attr == "sub-content-thread":
                        sub_content_thread(i, "", "")
                print()
                continue

            if "prons-entries-list" in attr:
                print_pron(elm)
                continue

            if "vrs" in attr:
                # can't get css element ::before.content like "variants" in the word "duel"
                child = elm.getchildren()[0]
                for c in child.iterchildren():
                    attr_c = c.get("class")
                    if attr_c == "il " or attr_c == "vl":
                        print_or_badge(c.text)
                        continue
                    if attr_c == "va":
                        if c.text is None:
                            for i in child:
                                print_class_va(i.text)
                        else:
                            print_class_va(c.text)

                        continue
                    if "prons-entries-list" in attr_c:
                        continue
                continue


# --- parse class "row headword-row header-ins" --- #
def row_headword_row_header_ins(node):
    """Print verb types. e.g. valued; valuing"""

    children = node.getchildren()[0].getchildren()[0]
    if "ins" in children.attrib["class"]:
        print_class_ins(children)
        print()


def print_vrs(node):
    for elm in node.iterchildren():
        elm_attr = elm.get("class")
        if elm_attr is not None and "badge mw-badge-gray-100 text-start text-wrap d-inline" in elm_attr:
            c_print(f"#[bold]{elm.text.strip()}", end="")
        else:
            for child in elm.iterdescendants():
                attr = child.get("class")
                if attr is not None:
                    if attr == "il " or attr == "vl":
                        print_or_badge(child.text)
                    elif attr == "va":
                        if child.text is None:
                            for i in child:
                                print_class_va(i.text)
                        else:
                            print_class_va(child.text)
                    elif "prons-entries-list" in attr:
                        print_pron(child)
                    else:
                        continue


# --- parse class "row headword-row header-vrs" --- #
def row_headword_row_header_vrs(node):
    """Print word variants. e.g. premise variants or less commonly premiss"""

    children = node.getchildren()[0].getchildren()[0] # class "entry-attr vrs"
    print_vrs(children)
    print()


# --- parse class "dxnls" --- #
def dxnls(node):
    """Print dxnls section, such as 'see also', 'compare' etc."""

    texts = list(node.itertext())
    for text in texts:
        text = text.strip()
        if not text:
            continue
        if text == "see also":
            c_print(f"\n#[bold {w_col.dxnls_content}]{text.upper()}", end = " ")
        elif text == "compare":
            c_print(f"\n#[bold {w_col.dxnls_content}]{text.upper()}", end = " ")
        elif text == ",":
            c_print(f"#[{w_col.dxnls_content}]{text}", end = " ")
        else:
            c_print(f"#[{w_col.dxnls_content}]{text}", end = "")

    print()


# --- parse class "dictionary-entry-[number]" --- #
def dictionary_entry(node):
    """Print one entry of the word and its attributes like plural types, pronounciations, tenses, etc."""

    print()
    for elm in node.iterchildren():
        elm_attr = elm.get("class")
        if elm_attr is not None:
            if "row entry-header" in elm_attr:
                row_entry_header(elm)
                continue

            if elm_attr == "row headword-row header-ins":
                row_headword_row_header_ins(elm)
                continue

            if elm_attr == "row headword-row header-vrs":
                row_headword_row_header_vrs(elm)
                continue

            if elm_attr == "vg":
                vg(elm)
                continue

            if "entry-uros" in elm_attr:
                for i in elm.iterchildren():
                    entry_uros(i)
                    print()
                continue

            if elm_attr == "dxnls":
                dxnls(elm)
                continue

            if elm_attr == "mt-3":
                badge = elm.getchildren()[0] # class "lbs badge mw-badge-gray-100 text-start text-wrap d-inline"
                print_header_badge(badge.text, end="\n")
                continue

            if elm_attr == "cxl-ref":
                text = list(elm.itertext())
                print_meaning_content(": ", end="")
                for t in text:
                    t = t.strip()
                    if t:
                        print_meaning_content(t, end=" ")
                print()
                continue


##############################
# --- print abstractions --- #
##############################

def print_meaning_badge(text, end=" "):
    c_print(f"#[{w_col.meaning_badge}]{text}", end=end)


def print_header_badge(text, end=" "):
    c_print(f"#[{w_col.meaning_badge}]{text}", end=end)


def print_meaning_arrow(text, end=" "):
    c_print(f"#[{w_col.meaning_arrow}]{text}", end=end)


def print_meaning_keyword(text, end=" "):
    c_print(f"#[{w_col.meaning_keyword}]{text}", end=end)


def print_meaning_content(text, end=""):
    if text == ": ":
        c_print(f"#[{w_col.meaning_content} bold]{text}", end=end)
    else:
        c_print(f"#[{w_col.meaning_content}]{text}", end=end)


def format_basedon_ancestor(ancestor_attr, prefix="", suffix=""):
    print(prefix, end="")
    if ancestor_attr == "sense has-sn has-num-only":
        print("  ", end=suffix)
    if ancestor_attr == "sense has-sn has-num":
        print("    ", end=suffix)
    if ancestor_attr == "sense has-sn":
        #if "no-sn letter-only" in root_attr:
        #    print("  ", end=suffix)
        print("    ", end=suffix)
    if ancestor_attr == "sense  no-subnum":
        print("", end=suffix)
    if ancestor_attr == "sense has-num-only has-subnum-only":
        print("    ", end=suffix)


def print_pron(node, header=False):
    sibling = node.getnext()
    before_semicolon = ((sibling is not None) and (sibling.get("class") == "sep-semicolon"))
    before_or = ((sibling is not None) and (sibling.get("class") == "il "))

    prons = []
    for text in node.itertext():
        text = text.strip("\n").strip()
        if text:
            prons.append(text)

    count = len(prons)
    if count == 1:
        if sibling is None:
            if header == True:
                print(f"|{prons[0]}|", end="\n") # e.g. fortissimo 1 of 2
            else:
                print(f"|{prons[0]}|", end="")   # e.g. fortissimo 2 of 2
        else:
            if before_semicolon or before_or:
                print(f"|{prons[0]}|", end="")
            else:
                print(f"|{prons[0]}|", end=" ")
    if count > 1:
        for index, pron in enumerate(prons):
            if index == 0:
                if before_semicolon or before_or:
                    print(f"|{pron}|", end="")
                else:
                    print(f"|{pron}|", end="  ")
            elif index == count - 1:
                if sibling is not None:
                    c_print(f"#[{w_col.eh_word_syllables}]{pron}", end=" ")
                else:
                    if header == True:
                        c_print(f"#[{w_col.eh_word_syllables}]{pron}", end="\n")
                    else:
                        c_print(f"#[{w_col.eh_word_syllables}]{pron}", end="")
            elif pron == "," or pron == ";":
                continue
            else:
                text = pron + ", "
                c_print(f"#[{w_col.eh_word_syllables}]{text}", end="")


def print_or_badge(text):
    c_print(f"#[{w_col.or_badge}]{text}", end = "")


def print_class_if(text, before_semicolon=False, before_il=False):
    if before_semicolon or before_il:
        c_print(f"#[bold]{text}", end="")
    else:
        c_print(f"#[bold]{text}", end=" ")


def print_class_va(text):
    c_print(f"#[bold]{text}", end=" ")


def print_class_sgram(node):
    for t in node.itertext():
        text = t.strip("\n").strip()
        if text and text.isalpha():
            c_print(f"#[bold]{t}", end=" ")


def print_class_ins(node):
    """print node whose class name includes ins, such as 'ins', 'vg-ins'."""
    for child in node:
        attr = child.get("class")
        if attr is not None:
            if attr == "il  il-badge badge mw-badge-gray-100":
                print_header_badge(child.text.strip(), end=" ")
            elif attr == "prt-a":
                print_pron(child)
            elif attr == "il ":
                print_or_badge(child.text)
            elif attr == "sep-semicolon":
                print(f"{child.text}", end="")
            elif attr == "if":
                next_sibling = child.getnext()
                if next_sibling is None:
                    print_class_if(child.text, before_semicolon=False)
                else:
                    sub_attr = next_sibling.get("class")
                    if sub_attr == "sep-semicolon":
                        print_class_if(child.text, before_semicolon=True)
                    elif sub_attr == "il ":
                        print_class_if(child.text, before_il=True)
                    else:
                        print_class_if(child.text, before_semicolon=False)
                global word_forms
                word_forms.append(child.text.strip().lower())
            else:
                c_print(f"#[bold]{child.text}", end="")


def print_dict_name():
    dict_name = "The Merriam-Webster Dictionary"
    c_print(f"#[{w_col.dict_name}]{dict_name}", justify="right")


###########################################################
# --- entry point for printing all entries of a word --- #
###########################################################

def parse_and_print(nodes, res_url, new_line=False):
    """Parse and print different sections for the word."""

    logger.debug(f"{OP.PRINTING.name} the parsed result of {res_url}")

    for node in nodes:
        try:
            attr = node.attrib["id"]
        except KeyError:
            attr = node.attrib["class"]

        if "-entry" in attr:
            dictionary_entry(node)

        if attr == "phrases":
            phrases(node)

        if attr == "nearby-entries":
            nearby_entries(node)

        if attr == "synonyms":
            synonyms(node)

        if "on-web" in attr:
            examples(node)

        if attr == "related-phrases":
            related_phrases(node)

    if new_line:
        print()
    # print_dict_name()


######################################################
# --- printing 'Word of the Day' --- #
######################################################

def print_wod_header(node):
    for elm in node.iterdescendants():
        attr = elm.get("class")
        if attr == "w-a-title":
            for c in elm.iterchildren():
                c_print(f"#[{w_col.wod_title} bold]{c.text}", end="")
            print()

        if attr == "word-header-txt":
            c_print(f"#[bold]{elm.text}")

        if attr == "main-attr":
            c_print(f"#[{w_col.wod_type}]{elm.text}", end="")
            print(" | ", end="")

        if attr == "word-syllables":
            c_print(f"#[{w_col.wod_syllables}]{elm.text}")


def print_wod_p(node):
    text = node.text
    if text:
        print(text, end="")

    for child in node.iterchildren():
        if child is not None and child.tag == "em":
            t = "".join(list(child.itertext()))
            c_print(f"#[bold]{t}", end="")
            print(child.tail, end="")
            continue
        if child is not None and child.tag == "a":
            child_text = child.text
            child_tail = child.tail
            if child_text == "See the entry >":
                continue
            else:
                if child_text is not None:
                    print(child_text, end="")
                for c in child.iterchildren():
                    if c is not None and c.tag == "em":
                        c_print(f"#[bold]{c.text}", end="")

            if child_tail is not None:
                print(child_tail, end="")
            continue
    print()


def print_wod_def(node):
    for elm in node.iterchildren():
        tag = elm.tag

        if tag == "h2":
            text = elm.text.strip("\n").strip()
            if text:
                c_print(f"\n#[{w_col.wod_subtitle} bold]{text}")
            children = list(elm.iterchildren())
            if children:
                child = children[0]
                tail = child.tail.strip("\n").strip()
                c_print(f"#[{w_col.wod_subtitle} bold]{child.text}", end=" ")
                c_print(f"#[{w_col.wod_subtitle} bold]{tail}", end="\n")

        if tag == "p":
            print_wod_p(elm)

        if tag == "div" and elm.attrib["class"] == "wotd-examples":
            child = elm.getchildren()[0].getchildren()[0]
            print_wod_p(child)


def print_wod_dyk(node):
    for elm in node.iterchildren():
        tag = elm.tag

        if tag == "h2":
            c_print(f"\n#[{w_col.wod_subtitle} bold]{elm.text}")

        if tag == "p":
            print_wod_p(elm)


def parse_and_print_wod(res_url, res_text):
    logger.debug(f"{OP.PARSING.name} {res_url}")

    parser = etree.HTMLParser(remove_comments=True)
    tree = etree.HTML(res_text, parser)
    s = """
    //*[@class="article-header-container wod-article-header"] |
    //*[@class="wod-definition-container"] |
    //*[@class="did-you-know-wrapper"]
    """

    nodes = tree.xpath(s)

    logger.debug(f"{OP.PRINTING.name} the parsed result of {res_url}")

    print()
    for node in nodes:
        attr = node.attrib["class"]

        if "header" in attr:
            print_wod_header(node)

        if "definition" in attr:
            print_wod_def(node)

        if "did-you-know" in attr:
            print_wod_dyk(node)
    print()
