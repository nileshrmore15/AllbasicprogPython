#--------------string reverse

strr = "4566"
print(strr[::-1])
list1 = list(strr)
print(list1)

'''------- Number typecast into list not possible
no = 6654
list2 = list(no)     # gives error because int object is not iterable
print(list2)
'''
#-------------- it convert list element to one string
temp = ''
for x in list1:
    temp = temp + x
print('temp : ', temp)


#------------------No. reverse
no = 4566

rev = 0
while no > 0:
    a = no % 10
    rev = rev * 10 + a
    no = no // 10

print(rev)