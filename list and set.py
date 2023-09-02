
l = [1,2,3,4,2,3,6]
s = set(l)
l2 = list(s)
print(l2)


set = { 1,2,3,4,5,6 }

set.add(7)
print(set)
set.remove(7)
print(set)

a = { 1,2,3,4,5,6 }
b = { 11,22,33,4,5,6 }
c= a.symmetric_difference(b)
print(c)
c= a.difference(b)
print(c)
c= b.difference(a)
print(c)
c= b.union(a)
print(c)
