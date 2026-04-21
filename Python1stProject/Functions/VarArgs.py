def sum(name,*elements):
    res=0
    print(name)
    for x in elements:
        res=res+x
    return res
print(sum("Atharva",1,2,3,4,5))
print(sum("Raj"))
print(sum("hari",1))