#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter,and finally displays
the body of the response.The email must be sent in the variable emai
"""
import sys
import requests


if __name__ == '__main__':
    values = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], values)
    print(r.text)
