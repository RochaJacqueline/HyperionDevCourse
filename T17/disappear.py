# Task 3

string = input("Please enter a string: ")
strip_chars = input("Which characters would you like to make disappear: ")

# Iterates over every character chosen by the user and replaces it on the string by an empty character
for char in strip_chars:
    string = string.replace(char, '')

print(string)