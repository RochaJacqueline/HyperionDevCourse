# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print("Welcome to the error program") # Syntax error: missing parentheses in the print function

print("\n") # Syntax error: missing parentheses in the print function and wrong indentation
# Syntax error: wrong indentation from line 10 to 15
ageStr = "24" #I'm 24 years old. # Syntax error: double equal symbol for variable declaration. Logical error: wrong string, should have only digits
age = int(ageStr)
print("I'm " + ageStr + " years old.") # Syntax error: wrong variable of type int "age" should be the string "ageStr"

three_and_half = 3.5 # Runtime error: wrong variable type string, should be int. # Logical error: 3 years and 6 months should be 3.5 years
answerYears = age + three_and_half

print("The total number of years: " + str(answerYears)) # Syntax error: missing parentheses in the print function, and missing casting answerYears to string
answerMonths = answerYears * 12 # Syntax error: variable answer not declared

print("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old") # Syntax error: missing parentheses in the print function, and missing casting answerMonths to string

#HINT, 330 months is the correct answer

