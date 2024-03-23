#!/usr/bin/python3
"""print all states that match the argument"""

import MySQLdb as sql
from sys import argv
if __name__ == '__main__':
    db = sql.connect(host="localhost",
                     port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE\
                BINARY name = '{}'".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
