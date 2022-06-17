year=int(input("enter year"))
if year%4==0 and year%100!=0:
    print(year,"is a leap year")
elif year%400==0:
    print(year,"is a centure year and leap year")
else:
    print(year,"is a normal year")