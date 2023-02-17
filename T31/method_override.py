# Compulsory task 2

#====Classes Section========
class Adult():
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        print(f"{self.name} is old enough to drive.")

class Child(Adult):
    def __init__(self, name, age, eye_colour, hair_colour):
        super().__init__(name, age, eye_colour, hair_colour)

    def can_drive(self):
        print(f"{self.name} is too young to drive.")

name = input("Please enter a name: ")
age = input("Please enter an age: ")
hair_colour = input("Please enter a hair colour: ")
eye_colour = input("Please enter an eye colour: ")

if age.isdigit() and int(age) >= 18:
    person = Adult(name, age, eye_colour, hair_colour)
    person.can_drive()
elif age.isdigit() and int(age) < 18:
    person = Child(name, age, eye_colour, hair_colour)
    person.can_drive()
else:
    print("You did not enter a valid age. Please try again")
