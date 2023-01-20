# Task 1

file = open('DOB.txt', 'r+')
names = []
birthdates = []

for line in file:
    split_data = line.split(" ")
    names.append(f"{split_data[0]} {split_data[1]}")
    birthdates.append(f"{split_data[2]} {split_data[3]} {split_data[4]}".rstrip("\n"))

file.close()

print("Name\n")

for name in names:
    print(name)

print("\nBirthdate\n")

for birthdate in birthdates:
    print(birthdate)