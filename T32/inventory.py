from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        #In this function, you must initialise the following attributes:
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        '''
        Returns the cost.
        '''
        return int(self.cost)

    def get_quantity(self):
        '''
        Returns the quantity.
        '''
        return int(self.quantity)

    def __str__(self):
        '''
        Returns a string representation of a class.
        '''
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"
    
    def set_quantity(self, quantity):
        '''
        Set a new quantity.
        '''
        if quantity >= 0:
            self.quantity = quantity
        else:
            print("This is not a valid quantity.")

#=============Shoe list===========

#List of objects of shoes
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        file = open("inventory.txt", "r")
        file_contents = file.readlines()
        # Iterates over the file_contents, and appends each shoe object to shoe_list
        for i in range(1, len(file_contents)):
            country, code, product, cost, quantity = file_contents[i].rstrip("\n").split(",")
            shoe = Shoe(country, code, product, cost, quantity)
            shoe_list.append(shoe)
        
    except:
        print("")
    finally:
        file.close()

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    # Prompts the user for a new shoe
    country = input("Please enter the name of the Country ")
    code = input("Please enter the product's code: ")
    product = input("Please enter the name of the product: ")
    cost = input("Please enter the cost of the product: ")
    quantity = input("Please enter the product's quantity: ")
    # Appends the shoe to shoe_list, and updates the inventory file
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    update_inventory()

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    # Creates shoe_strings list, and uses the list to print a table with all shoes
    shoe_strings = map(lambda shoe: str(shoe), shoe_list)
    table = map(lambda string: string.split(","), shoe_strings)
    print("")
    print(tabulate(table,headers=["Country", "Code", "Product", "Cost", "Quantity"]))
    print("")

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # Finds the first shoe object with least quantity
    shoe = min(shoe_list, key=lambda shoe: shoe.get_quantity())
    print(f"\nThe {shoe.product} with code {shoe.code} has the least quantity of {shoe.get_quantity()} items on stock.\n")
    # Prompts the user the change or not stock
    choice = input("Would you like to change this quantity (Y/N): ")

    if choice.lower() == "y":
        new_quantity = input("Enter the new quantity: ")
        # Sets a new quantity for this shoe stock in shoe_list, and updates the inventory file
        if new_quantity.isdigit():
            shoe.set_quantity(int(new_quantity))
            update_inventory()
        else:
            print("This is not a valid quantity. Please enter a number.")

def search_shoe(code):
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    search_result = None
    # Search for a shoe for a certain code
    for shoe in shoe_list:
        if shoe.code == code:
            search_result = shoe
            break
    # Prints an error if the code doesn't exist, or prints the shoe for this code
    if search_result == None:
        print("No shoe found with this code. Please try again.")
    else:
        print(f"{str(search_result)}\n")

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    # Prints the total value for each shoe in shoe_list
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print("")
        print(f"The total cost for {shoe.product} is {value}")
        print("")

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # Finds the shoe with the highest quantity and prints its information 
    shoe = max(shoe_list, key=lambda shoe: shoe.get_quantity())
    print(f"\nThe shoe {shoe.product} with {shoe.get_quantity()} items on stock costs {shoe.get_cost()}.\n")

def update_inventory():
    '''
    Opens inventory file and updades information for all shoes available in shoe_list
    '''
    file = open("inventory.txt", "w")
    for shoe in shoe_list:
        file.write(f"{str(shoe)}\n")
    file.close()

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
user_choice = ""
read_shoes_data()

while user_choice != "q":
    user_choice = input("""Choose an option from the menu below: 
    e - Enter a new shoe data
    v - View all shoes data
    r - Re_stock a shoe
    s - Search for a shoe with its code
    c - Calculate the total value for all shoes
    h - Highest quantity available for a shoe
    q - Quit the program
    """)

    if user_choice == "e":
        capture_shoes()

    elif user_choice == "v":
        view_all()

    elif user_choice == "r":
        re_stock()

    elif user_choice == "s":
        shoe_code = input("Please enter the shoe code that you want to search: ")
        search_shoe(shoe_code)

    elif user_choice == "c":
        value_per_item()

    elif user_choice == "h":
        highest_qty()

    elif user_choice == "q":
        print("You quit the program.")
    else:
        print("The option does not exist. Please try again and choose an option from the menu.")