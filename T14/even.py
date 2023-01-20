# Task 1

# Resquests and saves user's input in number
number = int(input("Please enter an integer number: "))
i = 1

# Prints all even numbers from 1 up to the number choosen by the user
while i <= number:

    if i % 2 == 0:
        print(i)

    i += 1
