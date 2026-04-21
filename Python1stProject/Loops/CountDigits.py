n=int(input())
k=0
if n==0:
    print("1")
else:
     while n!=0:
       k+=1
       n=n//10
     print(k)