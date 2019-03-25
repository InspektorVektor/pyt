import mysql.connector

def listmaker():
    a=[]
    for i in r:
        a.append(str(i))
        q='\n'.join(a)
    return q;

c = mysql.connector.connect(user="root", password="12345678", host="127.0.0.1",  database="base")
cursor = c.cursor()
cursor.execute("select title from table30")
r=cursor.fetchall()
print(listmaker())
c.commit()