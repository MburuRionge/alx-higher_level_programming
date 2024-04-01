#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
You must use the packages requests and sys
"""
import requests


def main(args):
    try:
        r = requests.get(args[1])
        print(r.headers['X-Request-Id'])
    except KeyError:
        pass


if __name__ == "__main__":
    import sys
    main(sys.argv)
