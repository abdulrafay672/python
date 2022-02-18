#Login form
name=input("Enter your Name")
email=input("Enter your Email")
password=input("Enter your PassWord")
age=input("Enter your Age")

print(name)
print(email)
print(password)
print(age)

if age == 1:
    print("TO Cast A Vote")
if age > 18:
    print("you are not eligible for cast a vote ")
if  age < 18:
    print("your vote has been cast")
"""
p=12345
abdul="abdulrafay"
if abdul == email or password == p :
    age=input("Enter your Age")
    if age == range(1):
        print("To cast a vote")
    elif age > range(1):
        print("You are not eligible for cast a vote")
    elif age < range(1) :
        print("Your vote Has been  cast")
else:
    print("YOur Email and Password Is Worng")

"""
    
    

