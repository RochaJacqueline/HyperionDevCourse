# Optional task

word = input("Please type a word: ")

# Compares the word with its reversed string, and prints if it is a palindrome or not
if word == word[::-1]:
    print("Your word is a palindrome.")
else:
    print("Your word is not a palindrome.")