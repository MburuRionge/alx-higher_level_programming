#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and
displays the body of the response. If the HTTP status code is greater than
or equal to 400,print: Error code:followed by the value of the HTTP status code
"""
import requests


def main(args):
    r = requests.get(args[1])
    try:
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError:
        print('Error code: {}'.format(r.status_code))

if __name__ == '__main__':
    import sys
    main(sys.argv)
