# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 15 Oct 2019
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
import argparse
import sys

choices = ["generate", ]

from mockr import generate


def main():
    parser = argparse.ArgumentParser(
        description="A Mock RESTful Web Server Generator.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "source",
        type=str,
        choices=choices,
        help="""\
- generate   : Generate Server Code.
- about   : About the Author.

"""
    )
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    source = args.source.lower()

    if source not in choices:
        vals = ", ".join(["'{}'".format(c) for c in choices])
        parser.error(
            "Unrecognized source '{}'. Valid entries are {}.".format(args.source, vals)
        )
    elif source == "generate":
        generate()


if __name__ == "__main":
    main()
