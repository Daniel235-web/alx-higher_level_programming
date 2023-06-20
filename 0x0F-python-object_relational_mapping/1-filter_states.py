#!/usr/bin/python3
"""
lists all states with starting name with N
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        passwd=argv[2], db=argv[3])
    cursor = con.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE left(name,1)='N'")
    db = cursor.fetchall()
    for i in db:
        print(i)
