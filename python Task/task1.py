print("Sr","   "," Item","    ","Item Price")
print("")
print("1","    "," Book","     ","120")
print("2","     "," Pen","      ","20")
print("3","    ","  beg","     ","700")
print("4","    "," Markur","     ","40")

my_item=[" ","book","pen","beg","markur"]

inp=int(input("Enter Order Sr Number"))
inp_q=int(input("Enter Quantity"))

if(inp==1):
    total=120*inp_q
    order= print("SR",inp,"BOOK", "    ","TOTAL Prk",total)
elif(inp==2):
    total=20*inp_q
    order=print("SR",inp,"Pen"," TOTAL PRk",total)
elif(inp==3):
    total=700*inp_q
    order=print("SR",inp,"BEG"," TOTAL PRK",total)
elif(inp==4):
    total=40*inp_q
    order=print("SR",inp,"MARKER"," TOTAL PRK",total)


print("Do you wan buy any thing else yes  press 1 no press")

inp2=input("YES/NO")
inp=int(input("Enter Order Sr Number"))
inp_q=int(input("Enter Quantity"))

if(inp2=="yes"):
    if(inp==1):
       total=120*inp_q
       print("SR",inp,"BOOK", "    ","TOTAL Prk",total)
    elif(inp==2):
         total=20*inp_q
         print("SR",inp,"Pen"," TOTAL PRk",total)
    elif(inp==3):
         total=700*inp_q
         print("SR",inp,"BEG"," TOTAL PRK",total)
    elif(inp==4):
         total=40*inp_q
         print("SR",inp,"MARKER"," TOTAL PRK",total)
elif(inp2=="no"):
    print("cancel")

else:
    print("no")

   
print(order)

