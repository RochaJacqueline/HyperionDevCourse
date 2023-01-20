# Task 2

import math

# Requests user's input and saves it in shape
shape = input("Please enter if the building shape is square, rectangular or round: ")
area = 0

# Creates conditions for each type of shape, requests user's input and calculates the area 
if shape.lower() == "square":
    
    length = float(input("Enter the length of the square: "))
    area = length * length

elif shape.lower() == "rectangular":
    
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = length * width

elif shape.lower() == "round":
    
    radius = float(input("Enter the radius of the circle: "))

    area = math.pi * (math.pow(radius, 2))

# Prints the area covered by the foundation
print(f"The area covered by the foundation of the building is: {area:.2f}")