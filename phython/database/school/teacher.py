import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database ='school'
    )
mycursor = mydb.cursor()

teacher=input("Teacher Name")
teacher_period=input("Enter teacher Period")
sql = "INSERT INTO teacher (teacher,teacher_period) VALUES ('"+teacher+"','"+teacher_period+"')"

print(sql)
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

print(mydb);
