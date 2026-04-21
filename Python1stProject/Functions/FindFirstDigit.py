# method 1 traditional do your self
#method 2
import math


def fun(a):
    return a//(10**int(math.log10(a)))
i=int(input("Number de\n"))
print(fun(i))