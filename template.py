#!/usr/local/bin/python2.7
""" template.py
template description
Usage:
      template.py (-f <file> | --file <file>)

Options:
    -h, --help      print out help message
    -v, --verbose   activate verbose output
"""
__author__ = 'olivier'
__title__ = 'template.py'
__version__ = '0.1'

try:
    from docopt import docopt
    import logging as log
except ImportError as ioex:
    log.error("Could not import a required module!")
    log.error(ioex)
    sys.exit(1)

def main():
    """
    main function
    """
    # gets arguments from docopt
    arguments = docopt(__doc__)
    # assigns docopt arguments
    verbose = docopt['--verbose']

    # set loglevel
    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output activated.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")
    log.info("Script was started with arguments: ")
    log.info(arguments)


if __name__ == "__main__":
    main()
