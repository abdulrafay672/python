def personal_info(name,f,Add,portal,Contact):
    print("Full Name :  ",name)
    print("F/Name :",f)
    print("Address : ",Add)
    print("portal Code :",portal)
    print("COntact_Number : ",Contact)

def educational_info(Qualification):
    print("Qualification :",Qualification)


def instit_delails(INSTITUTINAl,Batch,Course,Phase,Hold):
    print("INSTITUTINAl : ",INSTITUTINAl)
    print("Batch :",Batch)
    print("Course : ",Course)
    print("Phase : ",Phase)
    print("Hold By :",Hold)
    
name=input('Enter your name: ')
f=input("Enter your father Name")
Add=input("Enter your Address")
Portal=input("Enter your portal Code")
Contact=input("Enter your Contacrt Number")
Qualification=input("Enter your Qualification")
INSTITUTINAl=input("Enter your INSTITUTINAl Name")
Batch=input("Enter your Batch Name")
Course=input("Enter YOur Course Name")
Phase=input("Enter your Phase Name")
Hold=input("Enter your Hold By")

personal_info(name,f,Add,Portal,Contact)    
educational_info(Qualification)
instit_delails(INSTITUTINAl,Batch,Course,Phase,Hold)

