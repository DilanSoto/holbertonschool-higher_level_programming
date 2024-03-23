#!/usr/bin/python3
"""script that lists all cities with the state"""


import MySQLdb as sql
from sys import argv
if __name__ == '__main__':
    db = sql.connect(host="localhost", port=3306,
                     user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT cities.id, cities.name,\
    states.name FROM cities LEFT JOIN states\
    ON cities.state_id = states.id;"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
