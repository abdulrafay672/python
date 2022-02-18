import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database ='school'
    )
mycursor = mydb.cursor()

subject_name=input("student Name")
std_f_name=input("student Father Name")
roll=input("Your Roll Number")
sql = "INSERT INTO student (std_name,std_f_name,std_roll) VALUES ('"+subject_name+"','"+std_f_name+"','"+roll+"')"
print(sql)
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

print(mydb);
