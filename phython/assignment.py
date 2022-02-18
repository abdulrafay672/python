print("1 is Calculator")
print("2 is Marksheet")
print("3 is Odd And Even")
#print("4 is Season")
print("5 is Exit Porgram")


inp=int(input("Any One Number"))
if inp==1:
    plus="+"
    mines="-"
    multi="-"
    multi="*"
    dived="%"
    #def calul(plus,mines,multi,dived,remender):        
    first=int(input("Enter your 1st Value"))
    second=int(input("Enter your 1st Value"))
    mult=input("Select Sing")
    print("===========")
    if mult==plus:
            print(first+second)
    elif mult == mines:
             print(first-second)
    elif mult == multi:
            print(first*second)
    elif  mult == dived:
            print(first/second)
    elif mult == remender:
            print(first%second)
    
    #calul("+","-","*","/","%")

'''
def marksheet(name,eng,urdu,chemistry,biology,math,total):

    print("Full Name :  ",name)
    print("English ",eng)
    print("Urdu ",urdu)
    print("chemistry ",chemistry)
    print("Biology ",biology)
    print("Mathematics ",math)
    print("TOTAL MARKS ",total)


    name=input('Enter your name: ')
    eng=(input("Enter Your English Maks"))
    urdu=int(input("Enter Your Urdu Maks"))
    chemistry=int(input("Enter Your Chemistry Maks"))
    biology=int(input("Enter Your Biology Maks"))
    math=int(input("Enter Your mathematics Maks"))
    total=int(input("Enter Your Total Maks"))
    obtained=eng+urdu+chemistry+biology+math
    print(parsentage=obtained/total*100)
    
marksheet(name,eng,urdu,chemistry,biology,math,total)    
'''
if inp==2:
    name=input('Enter your name: ')
    #eng=int(input("Enter Your English Maks"))
    urdu=int(input("Enter Your Urdu Maks"))
    chemistry=int(input("Enter Your Chemistry Maks"))
    biology=int(input("Enter Your Biology Maks"))
    math=int(input("Enter Your mathematics Maks"))
    total=int(input("Enter Your Total Maks"))
    obtained=urdu+chemistry+biology+math
    parsentage=obtained/total*100

    print("===================")
    print("Full Name :  ",name)
    #print("English ",eng)
    print("Urdu ",urdu)
    print("chemistry ",chemistry)
    print("Biology ",biology)
    print("Mathematics ",math)
    print("===========================")
    print("TOTAL MARKS ",total)
    print("PARSENTAGE",parsentage)
    print("OBTAINED",obtained)
elif inp==3:
    ran=int(input("Enter your range "))
    print("==================")
    for a in range(ran):
        check=a%2
        
        if check==0:
            print(a,"Even ")
        else:
            print(a,"odd ")
elif inp==4:
    exit()
    

