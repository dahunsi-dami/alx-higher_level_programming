#!/usr/bin/python3
"""Takes arg, print rows where name match arg."""

if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
                WHERE BINARY states.name LIKE '{}'
                ORDER BY states.id ASC""".format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
