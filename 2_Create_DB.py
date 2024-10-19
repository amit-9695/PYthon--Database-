import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password='Amit@123')  # Connecting to the database
# obtain cursor object
cur=mydb.cursor()
# create a new database
cur.execute("CREATE DATABASE db1") 
