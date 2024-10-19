# Deleting a record from the database
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password='Amit@123', database='db1')  # Connecting to the database
# obtain cursor object
cur=mydb.cursor()
# delete data from the table
# write SQL delete query in a string variable
s="DELETE FROM book WHERE title='PHP'"
cur.execute(s)
# commit the changes to the database
mydb.commit()
# print the number of rows deleted
print(cur.rowcount, "record(s) deleted")