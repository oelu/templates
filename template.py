#!/usr/local/bin/python2.7
""" template.py
template description
Usage:
      template.py (-f <file> | --file <file>)

"""
__author__ = 'olivier'

# import statements
from docopt import docopt


def main():
    """
    main function
    """
    # gets arguments from docopt
    arguments = docopt(__doc__)
    # assigns docopt argumen
    print arguments


if __name__ == "__main__":
    main()
