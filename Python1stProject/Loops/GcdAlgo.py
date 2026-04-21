n=int(input())
m=int(input())
k=max(n,m)
l=min(m,n)

while k%l!=0:
    res=k%l
    k=l
    l=res
print(l)