
# find min and max element in list

a = [13, 12, 2, 5, 3, 3, 77, 66]

a.sort()

print("Min :", a[0])

print("Max :", a[-1])

# find sum of list

x = 0
for i in a:
    x = x + i
print("sum of list would be:", x)


# find min and max element in array
import array as ar

aa = ar.array('i', [-11, 3, 0, 33, 44, 322, 99, 22, 10])

mini = aa[0]
maxi = aa[0]
for i in range(1, len(aa)):
    if aa[i] < mini:
        mini = aa[i]
    if aa[i] > maxi:
        maxi = aa[i]

print("maximum no: ", maxi)
print("minimum no: ", mini)
