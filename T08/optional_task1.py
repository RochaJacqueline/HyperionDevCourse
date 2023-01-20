# Optional task 1

# Requests an integer and saves it in the variable number
number = int(input("Please type an integer number: "))

# Calculates the reminder of the number divided by 2, and if equal to zero prints that the number is even
if number % 2 == 0:
    print(f"{number} is even.")

else:
    print(f"{number} is odd.")