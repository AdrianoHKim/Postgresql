"""Obs.: Taken from PostgreSQL in Python - Crash Course (NeuralNine YouTube channel)

   - each time you run the code, remember to drop/delete the table.

"""


import psycopg2

conn = psycopg2.connect(host='aaaaa', dbname='bbbbbbb', user='ccccccs',
                        password='xxxxxxx', port=1111111)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person (
    id INT PRIMARY KEY,
    name VARCHAR(255), 
    age INT, 
    gender CHAR
); 
""")

cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
(1, 'Mike', 30, 'm'),
(2, 'Lisa', 30, 'f'),
(3, 'John', 54, 'm'),
(4, 'Bob', 80, 'm'),
(5, 'Julie', 40, 'f')
""")

cur.execute("""SELECT * FROM person WHERE name = 'Johny';""")

print(cur.fetchone())

cur.execute("""SELECT * FROM person WHERE age < 50;""")

for row in cur.fetchall():
    print(row)


sql = cur.mogrify("""SELECT * FROM person WHERE starts_with(name, %s) AND age < %s;""", ("J", 50))

print(sql)

cur.execute(sql)

print(cur.fetchall())

conn.commit()

cur.close()
conn.close()
