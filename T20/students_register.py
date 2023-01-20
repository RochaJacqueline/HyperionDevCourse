# Task 1

number_of_students = int(input("Enter how many students are registering: "))

file = open('reg_form.txt', 'w+')

# Writes the students ID in the file
for i in range(0, number_of_students):

    ID_number = input("Please enter your ID number: ")
    file.write(f"\n{ID_number}  ..................................\n")

# Resets the position to the beginning of the file
file.seek(0, 0)
student_register = file.read()
print(student_register)

file.close()

