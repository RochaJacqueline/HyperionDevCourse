# Optional task

words = []
vowels = ['a', 'e', 'i', 'o', 'u']
lines = 0

with open("input.txt", "r") as file:

    for line in file:
        words += line.rstrip("\n").split(" ")
        lines +=1

    print(f"Number of lines: {lines}")
    print(f"Number of words: {len(words)}")

    num_chars = 0
    num_vowels = 0

    for word in words:
        num_chars += len(word)
        for char in word.lower():
            if char in vowels:
                num_vowels += 1

    print(f"Number of characters: {num_chars}")
    print(f"Number of vowels: {num_vowels}")
