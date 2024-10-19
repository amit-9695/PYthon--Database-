# Extract dtypes from the data to use the fetchall() method
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password='Amit@123', database='db1')  # Connecting to the database
# obtain cursor object
cur=mydb.cursor()
# extract data from the table
# write SQL select query in a string variable
s="SELECT * FROM book"
cur.execute(s)
# fetch all the data from the table
result=cur.fetchall()
# print the data in the form of a list of tuples
for row in result:
    print(row)