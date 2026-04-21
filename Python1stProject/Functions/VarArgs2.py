def fun(name,**details): # uses Dictionary
    print(name)
    for d ,c in details.items():
        print(f"{d} is {c}")
fun("kap", drawback="Lack of punctuality", strength="Jhut bolna")
