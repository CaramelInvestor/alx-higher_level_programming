#!/usr/bin/python3
"""This script takes in an argument and
displays all values in the states table of
hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM state WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    query_row = cur.fetchall()
    for row in query_row:
        print(row)
