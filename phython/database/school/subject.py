import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database ='school'
    )
mycursor = mydb.cursor()

subject=input("subject Name")

sql = "INSERT INTO subject (subject_name) VALUES ('"+subject+"')"

print(sql)
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

print(mydb);
