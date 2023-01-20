names = ""

while True:

    name = input(" enter a name or 0 to quit or 1 to list names: ")

    if name == "0":
        break

    elif name == "1":
        print(names)
        continue

    names += f"{name}\n"

print(names)