# Task 2

# Resquests and saves user's inputs
start = int(input("What year do you want to start with? "))
years = int(input("How many years do you want to check? "))
print()

# Prints which year is a leap year or not, in a sequence given by the user
for i in range(start, start+years):

    if i % 4 != 0:
        print(f"{i} isn't a leap year.")
    else:
        print(f"{i} is a leap year.")
