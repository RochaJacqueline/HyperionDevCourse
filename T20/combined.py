# Task 2

numbers1 = open('numbers1.txt', 'r')
numbers2 = open('numbers2.txt', 'r')
all_numbers = open('all_numbers.txt', 'w+')

all_nums = []

# Appends all integers in numbers1 file to all_nums
for line in numbers1:
    all_nums.append(int(line))

# Appends all integers in numbers2 file to all_nums
for line in numbers2:
    all_nums.append(int(line))

all_nums.sort()

# Writes all sorted numbers in the all_numbers file
for n in all_nums:
    all_numbers.write(f"{n}\n")

numbers1.close()
numbers2.close()
all_numbers.close()
