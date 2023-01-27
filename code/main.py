import psycopg2
import pandas.io.sql as sqlio

#connect to db
try:
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")
    print("Connection success")
except Exception as e:
    print(e)

#test the connection
cur = conn.cursor()
cur.execute("SELECT * FROM public.siswa")

one = cur.fetchone()
all = cur.fetchall()
print(one)

conn.commit()

for i in all:
    print(i)

for record in all:
    print(record[0] ,"-", record[1])

data = sqlio.read_sql("SELECT * FROM public.siswa", conn)
data.head()