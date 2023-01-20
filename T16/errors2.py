# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

animal = "Lion" # Runtime error: missing double quotes
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # Logical error: missing format method, and wrong position of variables animal_type and number_of_teeth

print(full_spec) # Syntax error: missing parentheses in the print function
