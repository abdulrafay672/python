import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database ='student'
    )
mycursor = mydb.cursor()
name="rafay"
f_name="m_gulzar"
roll="12"
sql = "INSERT INTO std_data (std_name, std_f_name,std_roll_number) VALUES ('"+name+"','"+f_name+"',"+roll+")"
print(sql)
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

print(mydb);
