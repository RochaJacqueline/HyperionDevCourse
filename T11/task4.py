# Task 4

# Requests and saves user's input in number
number = int(input("Please enter an integer number: "))

# Analyses if number is divisible by 2 and 5, and prints result
if number % 2 == 0 and number % 5 == 0:

    print(f"{number} is divisible by 2 and 5.")

# Analyses if number is divisible by 2 or 5, and prints result
if number % 2 == 0 or number % 5 == 0:

    print(f"{number} is divisible by 2 or 5.")

# Analyses if number is not divisible by 2 or 5, and prints result
if number % 2 != 0 or number % 5 != 0:

    print(f"{number} is not divisible by 2 or 5.")