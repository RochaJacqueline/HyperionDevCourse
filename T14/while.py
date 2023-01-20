# Task 3

numbers = []
sum_numbers = 0

# Adds the user's input to numbers until they type -1
while True:

    numbers.append(int(input("Please enter a integer number: ")))

    if numbers[-1] == -1:
        break

# Sum all integers in numbers except for -1
for i in range(len(numbers)-1):
    sum_numbers += numbers[i]
    
# Prints the average of all numbers except for -1
print(sum_numbers/(len(numbers) - 1))