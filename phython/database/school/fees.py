import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database ='school'
    )
mycursor = mydb.cursor()

class_name=input("Class Name")
class_teacher=input("class Teacher Name")
sql = "INSERT INTO class (class_name,class_teacher) VALUES ('"+class_name+"','"+class_teacher+"')"

print(sql)
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

print(mydb);
