# Task 3

names = []

name = input("Please type a name: ")

# Requests and saves use's input in names, while name is different than John
while name.lower() != "john":
    names.append(name)
    name = input("Please type a name: ")
    
print(names)
