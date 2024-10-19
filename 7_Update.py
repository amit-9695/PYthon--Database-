# updating the data in the database
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password='Amit@123', database='db1')  # Connecting to the database
# obtain cursor object
cur=mydb.cursor()
# update data in the table
# write SQL update query in a string variable
s="UPDATE book SET price=price+100 WHERE title='Python'"
cur.execute(s)
# commit the changes to the database
mydb.commit()
# print the number of rows updated
print(cur.rowcount, "record(s) affected")
