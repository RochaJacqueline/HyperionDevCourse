# Task 3

str_manip = input("Please enter a setence: ")

# Prints the string's length
print(len(str_manip))

# Replaces all characters equal to the last with "@" and prints this new string
print(str_manip.replace(str_manip[-1],"@"))

# Prints the last three characters in reverse
print(str_manip[:-4:-1])

# Prints a word combining the first three characters in the string with the last two
print(f"{str_manip[:3]}{str_manip[-2::]}")

# Prints every word in a new line
print(str_manip.replace(" ", "\n"))