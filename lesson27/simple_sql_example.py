import psycopg2


connection = psycopg2.connect(user='postgres',
                              password='d2z76ctb',
                              host='localhost',
                              port='5432',
                              database='postgres'
                              )
cursor = connection.cursor()
#cursor.execute('CREATE TABLE usertablecoolfriends (id varchar(8) primary key, first_name varchar(25),last_name varchar(25), age integer,email varchar(50));COMMIT;')
#cursor.execute("INSERT INTO usertablecoolfriends (id, first_name, last_name, age, email) VALUES ('AAAAAAAA', 'Walter', 'White', 52, 'ww@gmail.com'), ('BBBBBBBB', 'Jessie', 'Pinkman',28, 'jp@gmail.com');COMMIT;")
cursor.execute('SELECT * from usertablecoolfriends;')
connection.commit()
fetched_result = cursor.fetchall()
for row in cursor.fetchall():
    print(row)
cursor.close()
if connection:
    connection.close()


