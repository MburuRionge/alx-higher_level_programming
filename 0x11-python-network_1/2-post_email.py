#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response
"""
import urllib.request
import urllib.parse


def main(args):
    url = args[1]
    values = {'email': args[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
    print(body.decode('utf-8'))


if __name__ == '__main__':
    import sys
    main(sys.argv)
