

## odd and even no.
list1 = [1,2,3,4,56,6,33,23]

list2 = [x for x in list1 if x % 2 == 0]

print("Even No:", list2)

list3 = [x for x in list1 if x % 2 != 0]

print("Odd no:", list3)
