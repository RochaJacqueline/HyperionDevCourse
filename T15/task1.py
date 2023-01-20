# Task 1

# Resquests and saves user's input in number
number = int(input("Please choose an integer number for the times table: "))
print()

# Prints times table for a number chosen by the user
for i in range(1, 13):

    print(f"{number} x {i} = {number * i}")