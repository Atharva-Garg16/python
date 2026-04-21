n=int(input())
b=True
for x in range(2,int(n**1/2)+1):
    if n%x==0:
        b=False
        break
if n==1:
    print("1 is god neither prime nor composite")
elif b:
    print("prime")
else:
    print("not a prime")