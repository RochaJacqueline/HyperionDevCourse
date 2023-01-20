# Task 2

numbers = []
max = 0

# Requests and saves 5 integers in numbers
while len(numbers) < 5:
    
    numbers.append(int(input("Please type an integer: ")))

print(numbers)

# Finds the largest integer in numbers
for i in range(0,3):
    if numbers[i] > max:
        max = numbers[i]

print(f"\nThe largest number in the sequence is {max}")