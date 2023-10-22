#!/usr/bin/python3
"""This script does what 2-my_filter_state.py
file does and is safe from MySQL injections"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    match = sys.argv[4]
    cur.execute("SELECT * FROM state WHERE name LIKE %s", (match, ))
    query_row = cur.fetchall()
    for row in query_row:
        print(row)
