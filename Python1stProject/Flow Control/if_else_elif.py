n=int(input("enter a number\n"))
if n>0:
    if n%2==0:
        print("even +ve")
    else:
        print("odd +ve")
elif n<0:
    if n%2==0:
        print("even -ve")
    else:
        print("odd -ve")
else:
    print(0)