import re

#pattern = r'^[A-Z]{4}[0-9]{1}[A-Z]{1}[0-9]{3}-[A-Z]{4}-[A-Z]{4}-[A-Z0-9]{10}$'
#pattern = r'^.{8}-.{4}-.{4}-.{12}$'

pattern = r'^[A-Z]{5}[0-9]{3}-[A-Z]{3}[0-9]{1}-[A-Z]{4}-[A-Z0-9a-z]{10}[0-9]{2}$'
string = 'ABCDX563-XHV4-VAXS-ZSCVXZCVXZ12'

match = re.match(pattern, string)
print(match)

if match:
    print("String matches the given pattern")
else:
    print("String does not match the given pattern")

# import re
#
# s = 'GeeksforGeeks: A computer science portal for geeks'
#
# match = re.search(r'portal', s)
#
# print('Start Index:', match.start())
# print('End Index:', match.end())
#
# #import re
#
# s = 'geeks.forgeeks'
#
# # without using \
# match = re.search(r'.', s)
# print(match)
#
# # using \
# match = re.search(r'\.', s)
# print(match)


# n=int(input("Enter number: "))
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# print("Reverse of the number:",rev)
#
# nn = str(5908)
# print(nn)
# c = nn[::-1]
# print(c)
