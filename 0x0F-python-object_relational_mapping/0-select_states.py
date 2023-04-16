#!/usr/bin/python3

import MySQLdb
import sys

""" listing all states from db in Ascending order
As you run this script, provide in this order
   mysql_username mysql_user_password, db_name

"""


def db_connect(username, password, db_name):
    host = "localhost"
    port = 3306
    charset = "utf8"
    conn = MySQLdb.connect(host=host,
                           port=port,
                           user=username,
                           passwd=password,
                           db=db_name,
                           charset=charset)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    db_connect(usr, pwd, db)
