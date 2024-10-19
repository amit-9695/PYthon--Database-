# Inser values from user
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password='Amit@123', database='db1')  # Connecting to the database
# obtain cursor object
cur=mydb.cursor()
# Taking user input
id=int(input("Enter book id: "))
t=input("Enter book title: ")
p=float(input("Enter book price: "))
# input query
s="INSERT INTO book (book_id, title, price) VALUES (%s, %s, %s)"
# input values
t=(id, t, p)
cur.execute(s, t)
mydb.commit()
print(cur.rowcount, "record inserted")
