import psycopg2
import csv

#connect to db
try:
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")
    print("Connection success")
except Exception as e:
    print(e)

cur = conn.cursor()

#create table latihan_users
try:
    cur.execute("""
                CREATE TABLE IF NOT EXISTS latihan_users(
                    id serial PRIMARY KEY,
                    email text,
                    name text,
                    phone text,
                    postal_code text
                )
    """
    )

    with open('source/users_w_postal_code.csv') as f:
        csv_reader = csv.reader(f, delimiter=',')
        next(csv_reader) #skip reader
        for row in csv_reader:
            cur.execute("INSERT INTO latihan_users VALUES (default, %s, %s, %s, %s) ON CONFLICT DO NOTHING", row)

    #insert using sql statements
    # cur.execute("INSERT INTO latihan_users VALUES (%s, %s, %s, %s,%s)", (1, 'hello@dataquest.io', 'Some Name','621234413', '12343'))

    conn.commit()
    print("Create table success")
except Exception as e:
    print(e)