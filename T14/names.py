# Task 2

names = []

# Adds a new name to names until the user types "stop", which breaks the loop
while True:

    names.append(input("Please type the names of all your pupils: "))

    if names[-1].lower() == "stop":
        break

print(names[:-1])
