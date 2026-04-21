def fun(num):
    li=[]; b=False
    for x in range(2,num//2+1):
        while num%x==0:
            b=True
            li.append(x)
            num=num//x
    if b:
        return li
    else:
        return [num]

k=int(input())
print(fun(k))
