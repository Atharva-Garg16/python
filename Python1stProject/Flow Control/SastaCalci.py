
print("""Operation you want to perform
1.Add
2.Subtract
3.multiply
4.Exponent
5.Divide""")
choice=int(input("select an option from 1 to 5\n"))
if choice not in [1,2,3,4,5]:
    print("invalid choice")
else:
    a=int(input("enter the 1st value"))
    b = int(input("enter the 2nd value "))
    if choice==1:
        print(a+b)
    elif choice==2:
        print(b-a)
    elif choice==3:
        print(b*a)
    elif choice==4 :
        print(b**a)
    else:
        print(b/a)
