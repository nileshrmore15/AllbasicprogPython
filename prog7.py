
# n array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
a = [-1, -3, 0, 1, 4, 4, 2, 6]
a.sort()
print(a)

b = []
for x in a:
    if x > 0 and x not in b:
        b.append(x)
print(b)

for i in range(1, len(b)):
    if i != b[i-1]:
        print(i)
        break

##---------------------------------------
def smallest_missing_integer(A):
    """
    Finds the smallest positive integer that does not occur in a given array A of N integers.
    """
    # First, we sort the array in ascending order.
    A.sort()

    # Initialize the missing integer to 1.
    missing_integer = 1

    # Iterate over the sorted array.
    for i in range(len(A)):
        # If the current element is negative or zero, skip it.
        if A[i] <= 0:
            continue

        # If the current element is equal to the missing integer, increment the missing integer.
        if A[i] == missing_integer:
            missing_integer += 1
        # If the current element is greater than the missing integer, we've found the smallest missing integer.
        elif A[i] > missing_integer:
            return missing_integer

    # If we haven't found the missing integer yet, it must be the next positive integer after the largest element in the array.
    return missing_integer


b = [-1, -3, 0, 1, 3, 4, 4, 2, 6]
c = smallest_missing_integer(b)
print(c)






