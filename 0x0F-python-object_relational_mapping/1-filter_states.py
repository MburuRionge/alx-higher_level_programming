#!/usr/bin/python3
"""its a function that filters states"""
import MySQLdb
import sys

def main(argv):
    if len(argv) != 5:
        print('Incorrect number of arguments')
        return

    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3]i,port=3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER_BY id ASC')

    for row in cur.fetchall():
        if row[1][0] == "N":
            print(row)

    db.close()


if __name__ == '__main__':
    main(sys.argv)
