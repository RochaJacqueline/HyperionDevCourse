# Optional task
import math

# Requests and stores the three sides of a triangle
print("Please type the three sides of a triangle")
side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

# Calculates the semi perimeter of the triangle with sides given by the user
s = (side1 + side2 + side3)/2

# Calculates the area of the triangle
triangle_area = math.sqrt((s * (s-side1) * (s-side2) * (s-side3)))

print(triangle_area)