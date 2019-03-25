import mysql.connector
c = mysql.connector.connect(user="root", password="12345678", host="127.0.0.1",  database="city")
cursor = c.cursor()
cursor.execute("select * from city")
r=cursor.fetchall()
for i in r:
    print(i)
c.commit()
