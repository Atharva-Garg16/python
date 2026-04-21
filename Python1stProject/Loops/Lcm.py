m=int(input())
n=int(input())
p=max(m,n)
q=min(m,n);i=1
while (i*p)%q!=0:
       i+=1
print(i*p)