import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='school_managment'
    )
mycursor=mydb.cursor()

roll=input("Enter Your Roll Name")
name=input("Enter Your Name")
f_name=input("Enter Your Father Name")
quali=input("Enter Your Name")
adders=input("Enter Your ADDERS")
age=input("Enter Your Age")
cnic=input("Enter Your CNIC Number")
Gender=input("Enter Your Gender \n Male / Female")
country=input("Enter Your Country Name")

sql="INSERT INTO intsert_data(std_name,std_f_name,std_roll,std_qualification,std_address,std_age,std_cnie,std_gender,std_country)value('"+roll+"','"+name+"','"+f_name+"','"+quali+"','"+adders+"','"+age+"','"+cnic+"','"+Gender+"','"+country+"')"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"Record Insert")
