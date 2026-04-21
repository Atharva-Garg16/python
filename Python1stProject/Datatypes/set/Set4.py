s={1,2,3,4,5}
s2={1,2,5,8,9}
# difference of sets
print(s - s2)
print(s.difference(s2))
# intersection of sets
print(s & s2)
print(s.intersection(s2))
#union of 2 sets
print(s|s2)
print(s.union(s2))
#is disjoint
print(s.isdisjoint(s2))
#symmetric difference
print(s^s2)
print(s.symmetric_difference(s2))


