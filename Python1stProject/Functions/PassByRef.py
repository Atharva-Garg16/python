def fun(l):
    l[1]=14 # ye original mai change kr rha h
    print(l)
    l=[10,20] # Ye Locally naya object ban rha h
    print(l)
l=[10,20,30]
print(l)
fun(l)
print(l)
