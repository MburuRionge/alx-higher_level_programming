#!/usr/bin/python3
"""A script that lists states"""
import MySQLdb
import sys


def main(argv):
    if len(argv) != 4:
        print("Incorrect number of arguments")
        return

    db = MySQLdb.connect(host='localhost', user=argv[1],
                            passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    row = cur.fetchall()
    for r in row:
        print(r)

    cur.close()
    db.close()


if __name__ == '__main__':
    main(argv)
