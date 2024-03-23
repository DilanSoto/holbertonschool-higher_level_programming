#!/usr/bin/python3

"""Script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb


if __name__ == '__main__':
    # Obtaining MySQL credentials from command-line arguments
    user, password, database = argv[1], argv[2], argv[3]
    # Connecting to MySQL database
    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=database)
    # Creating cursor object
    db = db.cursor()
    # Executing SQL query to select states starting with N and sorting by id
    db.execute("""SELECT * FROM states
    WHERE REGEXP_LIKE(name, '^N', 'c') ORDER BY id""")
    r = db.fetchall()
    for i in r:
        print(i)
