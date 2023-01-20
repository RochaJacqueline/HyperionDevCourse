# Optional task 2

def add_num():
    num1 = float(input("Please enter a number: "))
    num2 = float(input("Please enter a number: "))
    print(f"{num1} + {num2} = {num1 + num2}")

def subtract_num():
    num1 = float(input("Please enter a number: "))
    num2 = float(input("Please enter a number: "))
    print(f"{num1} - {num2} = {num1 - num2}")

def multiply_num():
    num1 = float(input("Please enter a number: "))
    num2 = float(input("Please enter a number: "))
    print(f"{num1} * {num2} = {num1 * num2}")

def divide_num():
    num1 = float(input("Please enter a number: "))
    num2 = float(input("Please enter a number different than zero: "))

    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("The second number can not be zero. Please try again.")

def menu_option():
    print("Option 1 - add")
    print("Option 2 - subtract")
    print("Option 3 - multiply")
    print("Option 4 - divide")

menu_option()    
option_number = int(input("Please choose an option number from 1 to 4: "))

if option_number == 1:
    add_num()
elif option_number == 2:
    subtract_num()
elif option_number == 3:
    multiply_num()
elif option_number == 4:
    divide_num()
else:
    print("Option number not valid. Please try again.")