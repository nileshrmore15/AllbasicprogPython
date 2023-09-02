
list_a = [10,20,20,30,40,20,50,30]

list_b = []

for x in list_a:
    if x not in list_b:
        list_b.append(x)

print(list_b)


list_c = list(set(list_a))

print(list_c)