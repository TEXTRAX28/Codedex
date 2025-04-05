numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 == 1]

print(f"Original numbers: {numbers}")
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")

