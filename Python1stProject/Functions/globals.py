def fun():
    x=10
    globals()['x']=20
    print(x)
x=13
print(x)
fun()
print(x)