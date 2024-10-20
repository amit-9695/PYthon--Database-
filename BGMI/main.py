# A mini project thatis ude to taking the user's input of BGMI playing time and date and storing it in the database.
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password='Amit@123', database='bgmi')  # Connecting to the database
mycursor = mydb.cursor()  # Creating a cursor object
# Creating a table
s="CREATE TABLE bgmi (id INT AUTO_INCREMENT PRIMARY KEY, date DATE, time TIME)"
mycursor.execute(s)
print("Table created successfully")
