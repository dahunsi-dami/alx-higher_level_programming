#!/usr/bin/python3
"""
Takes arg, print rows where state match arg in `cities`,
and parameterize query to prevent sql injection.
"""

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
    user_input = sys.argv[4]
    sql_query = """SELECT cities.name FROM cities
                LEFT JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC;"""
    cur.execute(sql_query, (user_input,))
    query_rows = cur.fetchall()
    nrows = len(query_rows)
    c = 0
    result = ''
    while c < nrows:
        result += str(query_rows[c])[2:-3]
        if c != nrows - 1:
            result += ', '
        c += 1
    print(result)
    cur.close()
    conn.close()
