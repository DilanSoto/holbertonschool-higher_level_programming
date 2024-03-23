#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state
"""


import MySQLdb as sql
from sys import argv
if __name__ == '__main__':
    db = sql.connect(host="localhost",
                     port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT cities.name FROM cities JOIN states ON\
    cities.state_id = states.id WHERE states.name = %s"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    cities_array = [row[0] for row in rows]
    cities_string = ", ".join(cities_array)
    print(cities_string)
    cur.close()
    db.close()
