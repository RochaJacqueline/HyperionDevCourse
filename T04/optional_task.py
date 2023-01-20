# Optinal task

# Requests input from user and saves 2 numbers 
num1 = int(input("Please type a number: "))
num2 = int(input("Please type a number: "))

print(num1)
print(num2)

# Switches values of the 2 numbers
num1 += num2
num2 = -num2 + num1
num1 -= num2 

print(num1)
print(num2)
