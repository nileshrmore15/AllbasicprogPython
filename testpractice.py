
def generate_even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


even_numbers = generate_even_numbers(30)

print(next(even_numbers))  # Output: 0
print(next(even_numbers))  # Output: 2
print(next(even_numbers))  # Output: 4

