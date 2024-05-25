import sqlite3
import logging
import argparse
import sys
import os
import subprocess

from .cache import (
    get_response_words,
    get_random_words,
    delete_word,
)
from .console import c_print
from .log import logger
from .utils import OP, DICT
from .dicts import webster, cambridge
from .__init__ import __version__

def parse_args():
    parser = argparse.ArgumentParser(
        description="Terminal Version of Cambridge Dictionary by default. Also supports Merriam-Webster Dictionary."
    )

    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="print the current version of the program",
    )

    # Add sub-command capability that can identify different sub-command name
    sub_parsers = parser.add_subparsers(dest="subparser_name")

    # Add sub-command l
    parser_lw = sub_parsers.add_parser(
        "l",
        help="list alphabetically ordered words/phrases you've found before",
    )

    # Make sub-command l run default funtion of "list_words"
    parser_lw.set_defaults(func=list_words)

    # Add an optional argument for l command
    parser_lw.add_argument(
        "-d",
        "--delete",
        nargs="+",
        help="delete a word/phrase or multiple words/phrases(separated by ', ') from cache",
    )

    # Add an optional argument for l command
    parser_lw.add_argument(
        "-t",
        "--time",
        action="store_true",
        help="list words/phrases you've found before in reverse chronological order",
    )

    # Add an optional argument for l command
    parser_lw.add_argument(
        "-r",
        "--random",
        action="store_true",
        help="randomly list 20 words/phrases you've found before",
    )

    # Add sub-command s
    parser_sw = sub_parsers.add_parser("s", help="look up a word/phrase; hidden for convenience, no need to type")

    # Make sub-command s run default function of "search_words"
    parser_sw.set_defaults(func=search_word)

    # Add positional arguments with n args for s command
    parser_sw.add_argument(
        "word_or_phrase",
        nargs="+",
        help="look up a word/phrase in Cambridge Dictionary; e.g. camb <word/phrase>",
    )

    # Add an optional argument for s command
    parser_sw.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="look up a word/phrase in debug mode",
    )

    # Add an optional argument for s command
    parser_sw.add_argument(
        "-w",
        "--webster",
        action="store_true",
        help="look up a word/phrase in Merriam-Webster Dictionary",
    )

    # Add an optional argument for s command
    parser_sw.add_argument(
        "-f",
        "--fresh",
        action="store_true",
        help="look up a word/phrase afresh without using cache",
    )

    # Add an optional argument for s command
    parser_sw.add_argument(
        "-c",
        "--chinese",
        action="store_true",
        help="look up a word/phrase in Cambridge Dictionary with Chinese translation",
    )

    # Add an optional argument for s command
    parser_sw.add_argument(
        "-n",
        "--nosuggestions",
        action="store_true",
        help="look up a word/phrase without showing spelling suggestions if not found",
    )

    # Add sub-command wod
    parser_wod = sub_parsers.add_parser(
        "wod",
        help="list today's Word of the Day from Merriam-Webster Dictionary",
    )

    # Make sub-command wod run default funtion of "wod"
    parser_wod.set_defaults(func=wod)

    # Add an optional argument for wod command
    parser_wod.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="list all words of the day",
    )

    if len(sys.argv) == 1:
        print_help(parser, parser_lw, parser_sw, parser_wod)

    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print_help(parser, parser_lw, parser_sw, parser_wod)

    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        print("cambridge " + __version__)
        sys.exit()

    elif sys.argv[1] == "l" or sys.argv[1] == "wod":
        args = parser.parse_args()

    else: # only for command "s"
        to_parse = []
        word = []
        for i in sys.argv[1 : ]:
            if i.startswith("-") and i[1] in ["-", "h", "d", "f", "w", "c", "n"]:
                to_parse.append(i)
            # NOTE
            # Python stdlib `parser.parse_args()` does not allow the value of an argument to start with "-", e.g. camb -w "-let"
            # Without the following workaround, Python interpreter will terminate the program  with the error:
            # `main.py s: error: the following arguments are required: word_or_phrase`
            # However, in terms of word lookup, you sometimes just want to know the meaning of a specific suffix like "-let"
            # Luckily, search without "-", the result of which can also contain the meaning of "-let" suffix
            elif i.startswith("-"):
                word.append(i[1 : ])
            else:
                word.append(i)

        to_search = " ".join(word)
        to_parse.append(to_search)
        args= parser_sw.parse_args(to_parse)
    return args


def print_help(parser, parser_lw, parser_sw, parser_wod):
    parser.print_help()
    print("\n\n\033[1mCOMMAND l\033[0m")
    parser_lw.print_help()

    print("\n\n\033[1mCOMMAND s (hidden)\033[0m")
    parser_sw.print_help()

    print("\n\n\033[1mCOMMAND wod\033[0m")
    parser_wod.print_help()

    sys.exit()


def delete(word, con, cur):
    deleted, data = delete_word(con, cur, word)

    if deleted and data is not None:
        for i in data:
            if "cambridge" in i[1]:
                print(f'{OP.DELETED.name} "{word}" from {DICT.CAMBRIDGE.name} in cache successfully')
            else:
                print(f'{OP.DELETED.name} "{word}" from {DICT.MERRIAM_WEBSTER.name} in cache successfully')
    else:
        print(f'{OP.NOT_FOUND.name} "{word}" in cache')


def print_word(index, entry):
    cols = os.get_terminal_size().columns
    text = entry[0]
    text_len = len(text)

    if "cambridge" in entry[1]:
        dict_name = "CAMBRIDGE"
    else:
        dict_name = "WEBSTER"

    if index % 2 == 0:
        print(f"\033[37;;40m{index+1:6d}|{text}", end="")
        print(f"\033[37;;40m{dict_name:>{cols-text_len-7}}\033[0m")

    else:
        c_print(f"#[#4A7D95]{index+1:6d}|{text}", end="")
        c_print(f"#[#4A7D95]{dict_name:>{cols-text_len-7}}")


def is_tool(name):
    """Check whether `name` is on $PATH and marked as executable."""

    from shutil import which
    return which(name) is not None


def fzf(data, con, cur):
    choices = {}
    for entry in data:
        choices[entry[0]] = entry[1]

    c = "\n".join(choices.keys())
    p1 = subprocess.Popen(["echo", c], stdout=subprocess.PIPE, text=True)
    p2 = subprocess.Popen(["fzf", "--layout=reverse"], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
    input_word = p2.communicate()[0].strip("\n")
    if p2.returncode == 130 and input_word == "": # press ESC, not word selected, quit out of fzf
        exit()
    if "merrian" in choices[input_word]:
        webster.search_webster(con, cur, input_word)
    else:
        cambridge.search_cambridge(con, cur, input_word)


def list_words(args, con, cur):
    # The subparser i.e. the sub-command isn't in the namespace of args

    if args.delete:
        to_delete = args.delete
        words = " ".join(to_delete)
        for w in words.split(","):
            i = w.strip()
            if i:
                delete(i, con, cur)

    elif args.random:
        try:
            data = get_random_words(cur)
        except sqlite3.OperationalError:
            logger.error("You may haven't searched any word yet")
        else:
            if not is_tool("fzf"):
                print()
                for index, entry in enumerate(data):
                    print_word(index, entry)
                print()
            else:
                fzf(data, con, cur)

    else:
        try:
            data = get_response_words(cur)
        except sqlite3.OperationalError:
            logger.error("You may haven't searched any word yet")
        else:
            if args.time:
                if not is_tool("fzf"):
                    data.sort(reverse=False, key=lambda tup: tup[2])
                    print()
                    for index, entry in enumerate(data):
                        print_word(index, entry)
                    print()
                else:
                    data.sort(reverse=True, key=lambda tup: tup[2])
                    fzf(data, con, cur)
            else:
                data.sort()
                if not is_tool("fzf"):
                    print()
                    for index, entry in enumerate(data):
                        print_word(index, entry)
                    print()
                else:
                    fzf(data, con, cur)


def search_word(args, con, cur):
    """
    The function is triggered when a user searches a word or phrase on terminal.
    First checks the args having "verbose" in it or not, if so, the debug mode will be turned on.
    Then it checks which dictionary is intended, and then calls respective dictionary function.
    """

    if args.debug:
        logging.getLogger(__package__).setLevel(logging.DEBUG)


    input_word = args.word_or_phrase[0].strip(".").strip(",").strip()

    if not input_word:
        print("You didn't input any word or phrase.")
        sys.exit()

    # boolean types
    is_webster = args.webster
    is_fresh = args.fresh
    is_ch = args.chinese
    no_suggestions = args.nosuggestions

    if is_webster and is_ch:
        print("Webster Dictionary doesn't support English to other language. Try again without -c(--chinese) option")
        sys.exit()

    if is_webster:
        webster.search_webster(con, cur, input_word, is_fresh, no_suggestions)
    else:
        cambridge.search_cambridge(con, cur, input_word, is_fresh, is_ch, no_suggestions)


def wod(args, con, cur):
    if args.list:
        print("Coming soon...")

    # no args supplied
    else:
        webster.get_wod()
