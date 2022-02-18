import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="school_managment"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM intsert_data")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
