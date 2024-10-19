import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password='Amit@123', database='db1')  # Connecting to the database
# obtain cursor object
cur=mydb.cursor()
# insert data into the table
# write SQL insert query in a string variable
s="INSERT INTO book (book_id,title,price) VALUES (%s,%s,%s)"  # %s is a placeholder
# create a list of tuples containing data that needs to be inserted into the table by replacing the placeholder %s
val=(2,'java',550)

# execute the query using the cursor object
cur.execute(s,val)
# commit the transaction
mydb.commit()
print("Data inserted successfully")

