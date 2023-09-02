### swapping of two numbers

# Input two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Print the numbers before swapping
print("Before swapping: a =", a, "and b =", b)

# Swap the numbers using a temporary variable
temp = a
a = b
b = temp

# Print the numbers after swapping
print("After swapping: a =", a, "and b =", b)


####--------------
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before swapping: a =", a, ", b =", b)

a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, ", b =", b)


