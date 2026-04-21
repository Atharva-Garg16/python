d={110:"abc", 101 : 'xyz', 105: "pqr", 106:"bcd"}
print(d)
d[101]="wxy"
print(d)
print(len(d))
print(d.pop(105))
print(d)
del  d[106]
print(d)
d[101]='not'
print(d.popitem())