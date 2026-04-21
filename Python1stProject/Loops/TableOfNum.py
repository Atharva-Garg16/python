#method 1
n=int(input("enter the number\n"))
m=int(input("enter how many multiples do you want to print\n"))
for x in range(1,m+1):
   print(n,"x",x,"=",n*x)
#method 2
print()
i=1
while i!=11:
    print(n,"x",i,"=",n*i)
    i+=1
