# Object-Oriented Programming: Classes

class CatObject():

    def __init__(self, name, breed, gender, age, is_asleep):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.age = age
        self.is_asleep = is_asleep

    def __str__(self):
        return f"Name: {self.name} \nBreed: {self.breed}\nGender: {self.gender}\nAge: {self.age}\nIs_asleep: {self.is_asleep}"

    def pet(self):
        return f"You pet {self.name}"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
    
bella = CatObject("Bella", "Siamese", "F", 12, False)
tabby = CatObject("tabby", "tabby", "M", 1, False)

cats = [bella, tabby]

for obj in cats:
    print(obj.get_name())

