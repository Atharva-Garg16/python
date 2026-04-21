year=int(input("enter year\n"))
if year%4==0 and year%100!=0 :
    print("leap year")
elif year%400==0:
    print("leap year")
else:
    print("normal year")
