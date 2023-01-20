# Optional task 2

# Requests and save user input
temperature = input("Is the temperature above 20 degrees? ")
weekend = input("Is today the weekend? ")
sunny = input("Is it sunny? ")

# Atributes true or false to temperature depending on user answer
if temperature.lower() == "yes":
    temperature = True
else:
    temperature = False

# Atributes true or false to weekend depending on user answer
if weekend.lower() == "yes":
    weekend = True
else:
    weekend = False

# Atributes true or false to sunny depending on user answer
if sunny.lower() == "yes":
    sunny = True
else:
    sunny = False

# Prints suggestion of shirt based on temperature value
if temperature:
    print("You should wear a short-sleeved shirt, ", end='')
else:
    print("You should wear a long-sleeved shirt, ", end='')

# Prints suggestion of bottoms based on weekend value
if weekend:
    print("shorts, ", end='')
else:
    print("jeans, ", end='')

# Prints suggestion of accessories based on sunny value
if sunny:
    print("and a cap.")
else:
    print("and a raincoat.")    
