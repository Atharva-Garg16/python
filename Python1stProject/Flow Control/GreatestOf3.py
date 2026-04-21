a=int(input("enter 1st value \n"))
b=int(input("enter 2nd value \n"))
c=int(input("enter 3rd value \n"))
print("the greatest of 3 values is" ,end=" ")
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
    #using of inbuilt function
print(max(a,b,c))