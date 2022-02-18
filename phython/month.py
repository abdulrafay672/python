month=12
weeks=4
week_days=7
week=3
day=29
days=30
#date=31+28+31+30+31+31+30+31+31+30+31+30+31
hours=24
mint=1440
second=86400

inp=int(input("Enter your YEAR"))

if month<=2000:
    print("Total Month in Year",month)
    print("Total week in year",weeks*month)
    print("Total Days in Year",days*month)
    print("Total Hours in Year",hours*360)
    print("Total Mint in Year",mint*month)
    print("Total Second in Year",second*month)
    
else:
 print("Your value is  rong")
