#!/usr/bin/python3
"""
Get my Github id """
import requests


def main(args):
    username = args[1]
    password = args[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(username, password))
    try:
        print(r.json().get('id'))
    except BaseException:
        pass


if __name__ == '__main__':
    import sys
    main(sys.argv)
