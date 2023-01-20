# Optional task

# Resquests and saves user's input in num
num = int(input("Please choose an integer number: "))

# If num is greater than 10, prints num the exact amount of times as its value. Otherwise prints a statement
if num > 10:
    for i in range(0, num):
        print(num)
else:
    print("\nSorry, too small")