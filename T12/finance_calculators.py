# Compulsory task 1: Capstone project

import math

# Requests user's input and saves in calculation_type
calculation_type = input("""Choose either 'investment' or 'bond' from the menu below to proceed:\n
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan\n\n""")

# Creates conditions to calculate acording to user's input
if calculation_type.lower() == "investment":

    # Requests all necessary input to calculate the total amount based on each type of interest
    deposit = float(input("\nPlease enter the amount of money you are depositing: "))
    interest_rate = float(input("Please enter the interest rate amount: "))
    years = int(input("Please enter the number of years you plan on investing: "))
    interest = input("Please enter if you want 'simple' or 'compound' interest: ")

    # Calculates and prints the total amount after simple interest rate
    if interest.lower() == "simple":

        total = deposit * (1 + (interest_rate/100) * years)
        print(f"\nThe amount after interest is {total}")
    
    # Calculates and prints the total amount after compound interest rate
    elif interest.lower() == "compound":

        total = deposit * math.pow(1 + (interest_rate/100), years)
        print(f"\nThe amount after interest is {total:.2f}")

# Calculates and prints the monthly amount payment on a home loan
elif calculation_type.lower() == "bond":

    house_value = float(input("\nPlease enter the house's value: "))
    annual_interest = float(input("Please enter the interest rate amount: "))/100
    months = int(input("Please enter the number of months you plan on repaying the bond: "))
    i = annual_interest / 12
    
    total = (i * house_value)/(1 - math.pow(1+i, -months))
    print(f"\nThe monthly payment is {total:.2f}")

else:
    print("\nYou did not chose a valid calculation type from the menu above. Start again.")
