# Task 1

import math

numbers = []

for i in range(0, 10):

    numbers.append(float(input("Please type a float: ")))

total = math.fsum(numbers)
print(f"The total of all numbers is: {total}")

min = min(numbers)
print(f"The index of the minimum is: {numbers.index(min)}")

max = max(numbers)
print(f"The index of the maximum is: {numbers.index(max)}")

average = round(total/len(numbers), 2)
print(f"The average of the numbers is: {average}")

numbers = sorted(numbers)

median = (numbers[4] + numbers[5])/2
print(f"The median of the numbers is: {median}")
