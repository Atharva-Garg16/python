d={110:'abc',115:112, 112:"bakri", 102:121.5 }
print(d)
print(d.get(115))
print(d.get(124))
print(d.get(124,"nhi hai"))
if 125 in d:
    print(d[125])
else:print('key not found')