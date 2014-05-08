#!/usr/local/bin/python2.7
""" restapy.py
template description
Usage:
      template.py (-h | --help )

"""
__author__ = 'olivier'

# import statements
from docopt import docopt
import requests
from pprint import pprint


def get_content():
    query_params = {'apikey': 'xxxx',
                    'key': 'value'
                    }
    endpoint = 'http://www.xyz.ch'

    response = requests.get(endpoint, params=query_params)
    data = response.json
    pprint(data)


def main():
    """
    main function
    """
    # gets arguments from docopt
    arguments = docopt(__doc__)
    get_content()


if __name__ == "__main__":
    main()
