# Task 3

num = 20

# Prints the count down from 20 to 0
while num >= 0:
    print(num)

    num -= 1

print()

# Prints the even numbers between 1 to 20
for i in range(2, 21, 2):
    print(i)

print()

# Prints a sequence made with asterisks
for i in range(1, 6):
    print(i * "*")

print()

# Resquests and saves user's input in num1 and num2
num1 = int(input("Please enter the first positive integer: "))
num2 = int(input("Please enter the second positive integer: "))
i = 0

# Saves the smallest between num1 and num2 in i
if num1 < num2:
    i = num1
else:
    i = num2

# Tests if num1 and num2 are divisible by the same number i, and stops the loop when i is the greatest common divisor
while not(num1 % i == 0 and num2 % i == 0):
    i -= 1

# Prints the greatest common divisor
print(i)
