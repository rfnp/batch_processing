import psycopg2

#connect to db
try:
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")
    print("Connection success")
except Exception as e:
    print(e)

cur = conn.cursor()

try:
    with open('source/users_w_postal_code.csv') as f:
        next(f) #skip reader
        cur.copy_from(f, 'latihan_users', sep=',', columns=('email', 'name', 'phone', 'postal_code'))

    conn.commit()
except Exception as e:
    print(e)