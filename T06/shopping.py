# Task 2

# Requests and stores the names of three products
print("Please type the name of three products")
product1 = input("Enter the first product: ")
product2 = input("Enter the second product: ")
product3 = input("Enter the third product: ")

# Requests and stores the prices of the three products
print("Please type the price of three products with two decimal digits")
price1 = float(input("Enter the first price: "))
price2 = float(input("Enter the second price: "))
price3 = float(input("Enter the third price: "))

# Calculates the total and average prices
total_price = price1 + price2 + price3
average_price = total_price / 3

print(f"The total of {product1}, {product2}, {product3} is £{round(total_price, 2)}, and the average price of the items is £{round(average_price, 2)}.")