import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password='Amit@123', database='db1')  # Connecting to the database
# obtain cursor object
cur=mydb.cursor()
# create a new table
# write SQL create table query in a string variable
s="CREATE TABLE book (book_id integer(4),title varchar(20),price float(5,2))"
# execute the query using the cursor object
cur.execute(s)
print("Table created successfully")