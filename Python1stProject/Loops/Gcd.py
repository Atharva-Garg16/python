import math

m=int(input())
n=int(input())
# q=min(m,n)
# for x in range(q,0,-1):
#     if m%x==0 and n%x==0:
#           break
#     else:continue
# print(x)
""" using inbuilt function """
gcd=math.gcd(m,n)
print(gcd)
