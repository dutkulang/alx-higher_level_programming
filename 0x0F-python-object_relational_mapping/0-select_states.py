#!/usr/bin/python3

import MySQLdb
import sys

""" listing all states from db in Ascending order
As you run this script, provide in this order
   mysql_username mysql_user_password, db_name

"""


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    conn = MySQLdb.connect(user=usr, passwd=pwd, db=db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
