# Task 1

# Requests and saves input from the user in the variables price and distance
price = float(input("Please enter the price of the package: ")) 
distance = float(input("Please enter the total distance in Km: "))

total_cost = price


delivery_method = input("Would you prefer air or freight? ")
# Determines the price of the prefered delivery method and adds to total price
if delivery_method.lower() == "air":
    total_cost += (0.36 * distance)
elif delivery_method.lower() == "freight":
    total_cost += (0.25 * distance)

insurance = input("Would you prefer full insurance or limited insurance? ")
# Determines the price of the prefered insurance and adds to total price
if insurance.lower() == "full insurance" or insurance.lower() == "full":
    total_cost += 50
elif insurance.lower() == "limited insurance" or insurance.lower() == "limited":
    total_cost += 25

gift = input("Would you prefer gift or no gift? ")
# Determines the price of the prefered option for gift and adds to total price
if gift.lower() == "gift":
    total_cost += 15

delivery_type = input("Would you prefer priority or standard delivery? ")
# Determines the price of the prefered delivery type and adds to total price
if delivery_type.lower() == "priority" or delivery_type.lower() == "priority delivery":
    total_cost += 100
elif delivery_type.lower() == "standard" or delivery_type.lower() == "standard delivery":
    total_cost += 20

# Prints the total cost
print(total_cost)
