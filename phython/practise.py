def create_account():
        data=("Abdul  Rafay",123,"abdulrafaykaimkhani")
        name=input("enter your name")
        password=int(input("enter your password"))
        email=input("enter your email")
        if email==data[2]:
           print("you have already account")
        else:
           print("your account has been created")
def update_account():
    
          name1=input("enter your name")
          password1=int(input("enter your password"))
          email1=input("enter your email")
          data=(name1,password1,email1)
          print("your account has been updated:")
def withdraw():
        withdraw=int(input("enter withdraw amount:"))
        balance=1000
        if(balance>=withdraw):
           print(withdraw,"amount successfully withdraw:")
           cur=(balance-withdraw)
           print(cur,"new balance")
        else:
            print("your amount is less!!")
def deposite():
        deposit=int(input("enter deposite amount:"))
        print(deposit,":amount has been deposited")
        balance=1000
        cur=(deposit+balance)
        print(cur,"new balance")
def balance():
        balance=1000
        print("your current balance is :",balance,"rupes")
def exite():
        print("you exited!!!")


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
    create_account()
elif (number==2):
    update_account()
elif number==3:
    withdraw()
elif number==4:
    deposite()
elif number==5:
    balance()
elif number==6:
    exite()
else :
    print("check out menu's list")
         
