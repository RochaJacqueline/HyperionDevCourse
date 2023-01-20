# Optional task

fav_rest = input("Please enter your favorite restaurant: ")

int_fav = int(input("Please enter you favorite number: "))

print(fav_rest)
print(int_fav)

""" The following statement causes an error (ValueError: invalid literal for int() with base 10: 'N') 
because it is not possible to convert a letter or words to an integer, since it doesn't represent numbers. 
An integer needs a digit to be valid.
"""
fav_rest = int(fav_rest)
