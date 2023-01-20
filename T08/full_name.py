# Task 2

# Requests and save the input in the variable full_name
full_name = input("Please enter your full name: ")
names = full_name.split()

# Tests conditions for the input to be a valid full name and prints accordingly
if len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure you have only entered your full name.")

elif len(full_name) == 0:
    print("You haven't entered anything. Please enter your full name.")

elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered you name and surname.")

elif len(names) < 2:
    print("Please enter name and surname")

else:
    print("Thank you for entering your name.")
    
