#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter,and finally displays
the body of the response.The email must be sent in the variable emai
"""
import requests


def main(args):
    r = requests.post(args[1], data={'email': args[2]})
    print(r.text)


if __name__ = '__main__':
    import sys
    main(sys.argv)
