#!/usr/bin/python3
"""takes arg and displays all vaues in states db matching the arg"""


import MySQLdb as sql
from sys import argv
if __name__ == '__main__':
    db = sql.connect(host="localhost",
                     port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name lIKE BINARY %s"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
