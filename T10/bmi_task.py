# Task 2

# Requests and saves input from user in variables weight and height
weight = float(input("Please enter your weight in Kg: "))
height = float(input("Please enter your height in meters: "))

# Calculates BMI
bmi = weight/(height*height)

# Creates conditions for different BMI ranges and prints statements for each case
if bmi >= 30:
    print(f"Your BMI is {bmi:.2f}, which indicates you are obese.")
elif bmi >= 25:
    print(f"Your BMI is {bmi:.2f}, which indicates you are overweight.")
elif bmi >= 18.5:
    print(f"Your BMI is {bmi:.2f}, which indicates your weight is normal.")
else:
    print(f"Your BMI is {bmi:.2f}, which indicates you are underweight.")
