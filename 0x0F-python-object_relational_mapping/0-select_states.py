#!/usr/bin/python3
"""This script ists all states from the database hbtn_0e_0_usa"""

import MySQLAlchemy
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")  # SQL command to grab states from db
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
