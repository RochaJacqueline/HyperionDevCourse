# Task 1

menu = ["coffee", "tea", "cake", "croissant"]

stock = {
    "coffee": 100,
    "tea": 75,
    "cake": 25,
    "croissant": 45,
}

price = {
    "coffee": 1.75,
    "tea": 1.25,
    "cake": 3,
    "croissant": 2.5,
}

stock_worth = 0

# Iterating over menu list, and adding the multiplication of each item stock per its price to total stock worth
for item in menu:

    stock_worth += stock[item] * price[item]

print(stock_worth)