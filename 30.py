import mysql.connector
c = mysql.connector.connect(user="root", password="12345678", host="127.0.0.1",  database="base")
cursor = c.cursor()
cursor.execute("select title from table30")
r=cursor.fetchall()
print(r)
c.commit()