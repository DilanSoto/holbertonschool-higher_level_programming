#!/usr/bin/python3
"""print all states from a database"""


import MySQLdb as sql
from sys import argv

if __name__ == '__main__':
    # Obtaining MySQL credentials from command-line arguments
    user, password, database = argv[1], argv[2], argv[3]
    # Connecting to MySQL database
 # Connecting to MySQL database
    db = MySQLdb.connect(host="localhost", user=u_name,
                         passwd=psw, db=base, port=3306)
    # Executing SQL query to select all states and sorting by id
    db.query("SELECT * FROM states ORDER BY id")
    r = db.store_result()
    t = r.fetch_row(maxrows=0)
    # Printing results
    for i in t:
        print(i)
    db = sql.connect(host="localhost",
                     port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
