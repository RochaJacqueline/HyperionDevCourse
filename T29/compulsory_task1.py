# Compulsory task 1: calculator

# Function that calculates operations with two numbers and returns a string representing the operation
def calculate(num1, num2, operator):

    result = f"{num1} {operator} {num2} = "   

    if operator == "+":
        result += f"{num1 + num2}"
    elif operator == "-":
        result += f"{num1 - num2}"
    elif operator == "*":
        result += f"{num1 * num2}"
    elif operator == "/":
        if num2 != 0:
            result += f"{num1 / num2}"
        else:
            result = ""

    return result + "\n"

# Function that opens and returns a file with name given by the user 
def open_history_file():
    while True:   
        file_name = input("Please enter the file name: ")
        try:
            new_file = open(file_name, "r")
            return new_file
        except FileNotFoundError:
            print("The file you are trying to open does not exist.")

# Function that prints every line in the file given by the user
def print_history(new_file):
    for line in new_file.readlines():
        print(line.strip("\n"))

file = open("history.txt", "a")
operators = ["+", "-", "*", "/"]
option = input("""Please choose an option:
1 - To make a calculation
2 - To view all calculations history\n
""")
if option.isdigit():
    if int(option) == 1:
        print("Please enter two integers and choose an operator for your calculation\n")
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        print("""\nPlease choose one of the operators:
        For addition: +
        For subtraction: -
        For multiplication: *
        For division: /
        """)
        operator = input("Enter one of the operators (+, -, *, or /): ")

        if num1.isdigit() and num2.isdigit():
            if operator in operators:
                print(calculate(int(num1), int(num2), operator))
                file.write(calculate(int(num1), int(num2), operator))
                file.close()
            else:
                print("You did not choose a valid operator. Please try again.")
        else:
            print("You did not choose two integers. Please try again.")

    if int(option) == 2:
        print_history(open_history_file())
