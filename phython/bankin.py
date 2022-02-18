print("**Banking Mangement**")
print("Menu")
print("1: Create Account:")
print("2: Update account")
print("3: Withdraw")
print("4: Deposite")
print("5: Balance")
print("6: exite")
number=int(input("enter menu's list number: "))
if (number==1):
    data=("Abdul  Rafay",123,"abdulrafaykaimkhani")
    name=input("enter your name")
    password=int(input("enter your password"))
    email=input("enter your email")
    if email==data[2]:
        print("you have already account")
    else:
        print("your account has been created")
elif (number==2):
    name1=input("enter your name")
    password1=int(input("enter your password"))
    email1=input("enter your email")
    data=(name1,password1,email1)
    print("your account has been updated:")
elif (number==3):
    print("lets start the process:")
    withdraw=int(input("enter withdraw amount:"))
    print(withdraw,"amount successfully withdraw:")
elif (number==4):
    deposit=int(input("enter deposite amount:"))
    print(deposit,":amount has been deposited")
elif (number==5):
    balance=1000
    print("your current balance is :",balance,"rupes")
elif (number==6):
    print("you exited!!!")
    
