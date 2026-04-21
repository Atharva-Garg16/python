n=int(input())
for x in range(n):
    for y in range(x):
        print(" ",end=" ")
    for k in  range(2*n-2*x-1):
        print("*",end=" ")
    print()