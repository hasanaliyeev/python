import psycopg2

conn = psycopg2.connect(dbname='testdb', user='postgres', password='hn19921995')

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS superheroes")
cur.execute("DROP TABLE IF EXISTS traffic_light")

conn.commit()

cur.execute("CREATE TABLE IF NOT EXISTS superheroes (hero_id serial PRIMARY KEY , hero_name varchar, strength int)")

conn.commit()

cur.execute("INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s)", ("Superman", 100))

conn.commit()

cur.execute("""
    INSERT INTO superheroes (hero_name, strength)
    VALUES (%(name)s, %(strength)s);
    """, {'name': 'Batman', 'strength': 200})

conn.commit()
d = {'name': 'Gasan Aliev', 'status': 'r', 'city': 'Volgodonsk'}
cur.execute("INSERT INTO customer (full_name, status, city) VALUES (%(name)s, %(status)s, %(city)s)",
            d)

conn.commit()

cur.execute("INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s)", ("Ironman", 100))
cur.execute("INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s)", ("Bahman", 100))

conn.commit()

cur.execute("SELECT * FROM superheroes")

one_line = cur.fetchone()
print(one_line, type(one_line))

full_line = cur.fetchall()
print(full_line)

conn.commit()
cur.close()
conn.close()

print(type(full_line[0][0]))
