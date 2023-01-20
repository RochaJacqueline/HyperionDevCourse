# Optional task

abbreviations = {
    "API": "Application Programming Interface",
    "IDE": "Integrated Development Environment",
    "SDK": "Software Development Kit",
    "UI": "User Interface",
}

# Adding abbreviations to the abbreviations dictionary
abbreviations["UX"] = "User Experience"
abbreviations["OOP"] = "Object-Oriented Programming"

user_abbreviation = input("Please enter an abbreviation: ")

# Comparing user's input with existing abbreviations in the dictionary
if user_abbreviation in abbreviations:
    print(f"\n{user_abbreviation}: {abbreviations[user_abbreviation]}")
else:
    print("Abbreviation not found.")