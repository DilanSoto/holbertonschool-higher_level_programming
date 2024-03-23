#!/usr/bin/python3

"""Script that lists all states from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    # Obtaining MySQL credentials from command-line arguments
    user, password, database = argv[1], argv[2], argv[3]
    
    # Connecting to MySQL database
    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=database)
    
    # Executing SQL query to select all states and sorting by id
    db.query("SELECT * FROM states ORDER BY id")
    r = db.store_result()
    t = r.fetch_row(maxrows=0)
    
    # Printing results
    for i in t:
        print(i)
