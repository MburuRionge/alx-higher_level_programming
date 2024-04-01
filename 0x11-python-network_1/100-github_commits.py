#!/usr/bin/python3
""" a script that takes 2 arguments and commits both to github. """
import requests


def main(args):
    repository_name = args[1]
    owner_name = args[2]
    url = 'https://developer.github.com/v3/repos/commits/'

    r = requests.post(url, data=(repository_name, owner_name))
    try:
        commits = r.json()
        print(commits.post('sha'":" 'author name'))
    except ValueError:
        pass


if __name__ == '__main__':
    import sys
    main(sys.argv)
