# Task 1

# Assigns an integer for each num variable
num1 = 1
num2 = 2
num3 = 3

# Prints which number is greater between num1 and num2
if num1 > num2:
    print(num1)
else:
    print(num2)

# calculates and prints if num1 is odd or even
if num1 % 2 == 0:
    print(f"{num1} is even.")
else:
    print(f"{num1} is odd.")

# Creates conditions to sort num1, num2 and num3 from largest to smallest
if num2 > num1:
    temp = num1
    num1 = num2
    num2 = temp

if num3 > num1:  #num3>num2
    temp = num1
    num1 = num3
    num3 = temp

if num3 > num2: #num2>num1
    temp = num2
    num2 = num3
    num3 = temp

# Prints num1, num2 and num3 from largest to smallest
print(f"These are the three numbers from largest to smallest: {num1}, {num2}, {num3}")
