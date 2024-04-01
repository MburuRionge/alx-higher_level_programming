#!/usr/bin/python3
"""Displays the value of X-Request-ID"""
import urllib.request


def main(args):
    if len(args) == 2:
        req = urllib.request.Request(args[1])
        with urllib.request.urlopen(req) as response:
            header = response.info()
            print(header['X-Request-Id'])


if __name__ == "__main__":
    import sys
    main(sys.argv)
