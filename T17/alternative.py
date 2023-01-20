# Task 1

string = input("Please type a phrase: ")
split_string = string.split()

# Iterates over split_string and changes each alternate character to upper or lower case
for i in range(len(split_string)):
    new_str = ""
    for j in range(len(split_string[i])):
        if j % 2 == 0:
            new_str += split_string[i][j].upper()
        else:
            new_str += split_string[i][j].lower()
    split_string[i] = new_str

print(' '.join(split_string))

# Iterates over split_string and changes each alternate word to lower or upper case
for i in range(len(split_string)):
    if i % 2 == 0:
        split_string[i] = split_string[i].lower()
    else:
        split_string[i] = split_string[i].upper()

print(' '.join(split_string))
