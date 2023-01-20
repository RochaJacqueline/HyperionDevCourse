# Task 3

import math
    
def minimum(integers):
    return min(integers)

def maximum(integers):
    return max(integers)

def avg(integers):
    return math.fsum(integers)/len(integers)

def percentile(number,integers):
    return (number/100) * len(integers)

# Learned I had to use UTF-8-SIG encoding because of the presence of BOM character at the start of the file.
input_file = open("input.txt", "r", encoding='utf-8-sig')
output_file = open("output.txt", "w+")

for line in input_file:
    input_list = line.split(",")
    # Separating the letters from number in the first element 
    input_list[0] = input_list[0].split(":")
    # Saving only the letters describing the math operation in the variable operation
    operation = input_list[0][0]
    # Saving all numbers in order in the input_list
    input_list[0] = input_list[0][1]
    # Converting numbers from string to int and saving in input_list
    input_list = list(map(int, input_list))

    if operation == "min":
        output_file.write(f"The {operation} of {input_list} is: {minimum(input_list)}.\n")
        print(f"The {operation} of {input_list} is: {minimum(input_list)}.\n")
    
    elif operation == "max":
        output_file.write(f"The {operation} of {input_list} is: {maximum(input_list)}.\n")
        print(f"The {operation} of {input_list} is: {maximum(input_list)}.\n")

    elif operation == "avg":
        output_file.write(f"The {operation} of {input_list} is: {avg(input_list)}.\n")
        print(f"The {operation} of {input_list} is: {avg(input_list)}.\n")

    elif "p" in operation:
        number = int(operation.strip("p"))
        output_file.write(f"The {number}th percentile of {input_list} is: {percentile(number, input_list)}.\n")
        print(f"The {number}th percentile of {input_list} is: {percentile(number, input_list)}.\n")

input_file.close()
output_file.close()
