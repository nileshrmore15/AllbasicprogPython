
# a = 33
#
# x = 0
# y = 1
# print(x)
# print(y)
#
# for i in range(1, a+1):
#     z = x + y
#     print(x+y)
#     x = y
#     y = z


# '''alternate fibonaci program'''
# def fibonacci(limit):
#     a, b = 0, 1
#     while a < limit:
#         print(a)
#         a, b = b, a + b
#
# # Example usage:
# fibonacci(10)  # Output: 0 1 1 2 3 5 8
#
# def fibonaci (limit):
#     a = 0
#     b = 1
#     while a < limit:
#         print(a)
#         c = a+b
#         a = b
#         b = c

# fibonaci(10)
#
# def fibonacii (limit):
#     a = 0
#     b = 1
#     count = 1
#     while count < limit:
#         count = count + 1
#         print(a)
#         c = a+b
#         a = b
#         b = c
#
# fibonacii(20)
#
#
# def factorial(nn):
#     a = 1
#     for i in range(1, nn+1):
#         a = a * i
#     print("factorial no: ", a)
#
# factorial(5)

def factoriall(nn):
    if(nn<=1):
        return 1
    return nn * factoriall(nn-1)

print("fatorial No: ", factoriall(5))

#
# list1 = [1,3,5,7,9,2,4,6,8,10]
# list2 =  [x for x in list1 if x%2 == 0]
# print("Even no: ", list2)
# list3 = [x for x in list1 if x%2 != 0]
# print("Even no: ", list3)
#
#
