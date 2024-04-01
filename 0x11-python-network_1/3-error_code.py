#!/usr/bin/python3
""" 
takes in a URL, sends a request to the URL and displays the body of the
response (decoded in utf-8).manage urllib.error.HTTPError exceptions and
print: Error code: followed by the HTTP status code
"""
import urllib.request


def main(args):
    url = args[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.URLError as e:
        print('Error code: {}'.format(e.code))


if __name__ == '__main__':
    import sys
    main(sys.argv)
