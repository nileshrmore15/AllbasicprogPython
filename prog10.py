### Prime No.


# def is_prime(num):
#     for i in range(2, num):
#         if num <= 1 or num % i == 0:
#             print("This is not prime no.")
#             break
#         elif num == i+1:
#             print("This is prime No.")
#
#
# a = int(input("Enter no: "))
# is_prime(a)

#----------------------

def is_primee(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(1,1001):
    if is_primee(i):
        print(i)

# print(is_primee(7))  # True
# print(is_primee(10)) # False
# print(is_primee(31)) # True