# Task 1

# Resquests user's age and saves the value in the variable age
age = int(input("Please type your age: "))

# Creates conditions acording to age's value and prints a statement for each case
if age >= 18:
    print("You are old enough!")
elif age > 16 and age < 18:
    print("Almost there.")
else:
    print("You're just too young!")