# Optional task

total_wage = 0

# Requests and saves user's input in the variable employee
employee = input("Please enter if you are a salesperson or a manager: ")

# Creates conditions and calculates the salary for each type of employee
if employee.lower() == "salesperson":

    gross_sales = float(input("Please enter the value of your gross sales for the month: "))
    total_wage = (0.08 * gross_sales) + 2000

else:
    hours_worked = float(input("Please enter the total hours worked per month: "))
    total_wage = 40 * hours_worked

print(total_wage)