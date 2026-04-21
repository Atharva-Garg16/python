n=int(input())
for x in  range(2,n+1):
    if n%x==0:
        break
    else:
        continue
print(x)