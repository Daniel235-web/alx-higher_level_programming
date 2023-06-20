#!/usr/bin/python3

"""
a script that lists all the states from the database
Usage: ./0-select_states.py <mysql username> <mysql password> <database>
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states")
    db = cursor.fetchall()
    for i in db:
        print(i)
