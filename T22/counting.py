# Task 3

string_input = input("Please type a sentence: ")
letter_occurrence = {}

# iterating over string_input list, and adding each letter and its occurrence to letter_occurrence dictionary
for char in string_input:

    if char in letter_occurrence:
        letter_occurrence[char] += 1
    else:
        letter_occurrence[char] = 1

print(letter_occurrence)
