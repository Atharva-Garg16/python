def sum_multi(a,b):
    return a+b,a*b
print(sum_multi(12,13))
### it returns as tuple we can also return as a list
def fun(a,b):
    return [a*b,a+b]
print(fun(12,13))
s,m=fun(23,45)
print(s)
print(m)