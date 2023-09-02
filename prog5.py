

## unique value in list

a = [10, 20, 30, 10, 20]
b = []

for x in a:
    if x not in b:
        b.append(x)

print(b)


# second way using set

a = [10, 20, 30, 10, 20]
b = set(a)
c = []

for x in b:
    c.append(x)

print(c)

