import mysql.connector  # Importing the mysql.connector module
mydb = mysql.connector.connect(host="localhost", user='root', password='Amit@123', database='PgEg')  # Connecting to the database
print(mydb)  # Printing the connection object
print(mydb.is_connected())  # Printing the connection status
print(mydb.database)  # Printing the database name
print(mydb.user)  # Printing the username
print(mydb.connection_id)  # Printing the connection id