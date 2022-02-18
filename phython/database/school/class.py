import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database ='school'
    )
mycursor = mydb.cursor()

month_fees=input("Month Fees")
year_fees=input("year fees")
sql = "INSERT INTO class (month_fees,year_fees) VALUES ('"+month_fees+"','"+year_fees+"')"

print(sql)
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

print(mydb);
