#!/usr/bin/python3
"""Defines a function to fetch a url"""
import urllib.request


def main():
    req = urlib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        body = response.read()

    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
    print('\t- utf8 content: {}'.format(body.decode('utf8')))


if __name__ == "__main__":
    main()
