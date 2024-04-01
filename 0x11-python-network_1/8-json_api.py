#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter. The letter must be sent in the variable q
If no argument is given, set q="", If the response body is properly JSON
formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise: Display Not a valid JSON if the JSON is invalid or 
Display No result if the JSON is empty
"""
import requests


def main(args):
    if len(args) == 1:
        data = ""
    else:
        data = args[1]

    r = requests.post( 'http://0.0.0.0:5000/search_user', data={'q': data})
    try:
        json = r.json()
        if json:
            print('[{}] {}'.format(json['id'], json['name'])
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')


if __name__ == '__main__':
    import sys
    main(sys.argv)
