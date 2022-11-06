import psycopg2
from psycopg2.extras import RealDictCursor, execute_values


with psycopg2.connect(dbname="project", user='postgres', password="hn19921995") as conn:
    with conn.cursor(cursor_factory=RealDictCursor) as curs:
        execute_values(curs, 'INSERT INTO "user" (user_name, user_password, full_name) VALUES %s',
                       [('adlisssev3', 'dg6675267', 'Gasan Aliev'), ('usdssser 3', '635673', 'Farid Aliev')])

        curs.execute('SELECT * FROM "user" ')
        records = curs.fetchall()
        print(records)
        print(records[0]["user_name"])
