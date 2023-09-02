

v = 'ABCDX563-XHV4-VGXS-ZXCVXZCVXZ12'
print(len(v))

a = []


def stringcheck(str):
    if len(str) == 16:
        for i in range (1,len(v)+1):
            a[i-1] = v[i-1]

        print(a)
  #  elif:
   #     print("string is not valid")
stringcheck(v)


##############################

import re

pattern = r'^[A-Z]{4}[0-9]{1}[A-Z]{1}[0-9]{3}-[A-Z]{4}-[A-Z]{4}-[A-Z0-9]{10}$'

string = 'ABCDX563-XHV4-VGXS-ZXCVXZCVXZ12'

match = re.match(pattern, string)

if match:
    print("String matches the given pattern")
else:
    print("String does not match the given pattern")


#####################################

import re

text = "The quick brown fox jumps over the lazy dog"
# pattern start with The and end with dog
pattern = r'^The.*dog.$'

match = re.match(pattern, text)
if match:
    print("String matches the given pattern")
else:
    print("String does not match the given pattern")


pattern = "q\w+"

# Search for a word that starts with "q"
match = re.search(pattern, text)
if match:
    print("Found:", match.group(0))

# Find all words that start with "q"
matches = re.findall(pattern, text)
print("Matches:", matches)

# Replace all occurrences of "quick" with "slow"
new_text = re.sub("quick", "slow", text)
print("New text:", new_text)

#############################

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

print(factorial(5))

def prime_no(num):
    for i in range(2,num):
        if i<= 0  or num % i == 0:
            print("This is not prime no")
            break
        elif i+1 == num:
            print("This is prime no")

nn= int(input("Enter no:"))
prime_no(nn)

strin= 'abc123$'
aa = []
for i in strin:
    if i == '1' or i == '2' or i == '3':
       aa.append(i)

print(aa)

list1 = [1,2,3,1,2,3,4,5,6,3,8,5,2,5]

list2 = set(list1)
print(list2)
dict = {}

for x in list2:
    count = 0
    for y in list1:
        if x == y:
            count = count +1
    dict.update({x:count})

print(dict)

import re

pattern = r'^[A-Z]{4}[0-9]{1}[A-Z]{1}[0-9]{3}-[A-Z]{4}-[A-Z]{4}-[A-Z0-9]{10}$'

string = 'ABCDX563-XHV4-VGXS-ZXCVXZCVXZ12'

match = re.match(pattern, string)

if match:
    print("String matches the given pattern")
else:
    print("String does not match the given pattern")

