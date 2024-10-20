# inserting data into the database
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password='Amit@123', database='bgmi')  # Connecting to the database
mycursor = mydb.cursor()  # Creating a cursor object
# Taking the input from the user
date = input("Enter the date in the format YYYY-MM-DD: ")
time = input("Enter the time in the format HH:MM: ")
# Inserting the data into the table
s = "INSERT INTO bgmi (date, time) VALUES (%s, %s)"
val = (date, time)
mycursor.execute(s, val)
mydb.commit()
print("Data inserted successfully")
