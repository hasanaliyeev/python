import psycopg2

connection = psycopg2.connect(dbname='project', user='postgres', password='hn19921995')
curs = connection.cursor()

curs.execute('SELECT * FROM person')
print(curs.fetchall())