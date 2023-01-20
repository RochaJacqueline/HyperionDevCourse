# Optional task

# Resquests and saves user's input in number
number = int(input("Please enter a number less than or equal to a 100: "))

# Continuously asks input if number is greater than 100, and if it is less than 100 prints a statement and breaks the look 
while True:

    if number > 100:
        number = int(input("The number was greater than 100, please enter again a number less than or equal to a 100: "))

    if number <= 100:

        if number % 2 == 0:
            print(number*2)
        else:
            print(number*3)

        break
