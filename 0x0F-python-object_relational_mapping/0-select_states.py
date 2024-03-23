#!/usr/bin/python3
"""A script that lists states"""
import MySQLdb
import sys


if __name__ == '__main__':
    """check if number of arguments provided is enough."""
    if len(sys.argv) != 5:
        print("Incorrect number of arguments")
        sys.exit(1)

    db = MySQLdb.connect(host='localhost', user=argv[1],
                            passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    row = cur.fetchall()
    for r in row:
        print(r)

    db.close()
