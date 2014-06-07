#!/usr/bin/python
""" filter.py
Parses standard input or files passed as arguments
Usage:
      filter.py file1 file2
      cat file1 | filter.py

Example:
    $ echo "hello world" | ./filter.py
    hello world

"""
__author__ = 'olivier'

import fileinput


def main():
    """
    main function
    """

    for line in fileinput.input():
        # do someting with line
        print line


if __name__ == "__main__":
    main()
