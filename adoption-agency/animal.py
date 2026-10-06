class Animal:
     name = ""
     age = 0
     sex = ""
     type = ""
     temperament = ""
     color = ""
     adopted_by = ""

     def __init__(self, name, age, sex, type, temperament, color):
        self.name = name
        self.age = age
        self.sex = sex
        self.type = type
        self.temperament = temperament
        self.color = color

     def adopt(self, by_person):
         self.adopted_by = by_person

     def is_adopted(self):
         if self.adopted_by == "":
            return False
         return True

     def info(self):
         print(f"Name: {self.name}")
         print(f"Age: {self.age}")
         print(f"Sex: {self.sex}")
         print(f"Type: {self.type}")
         print(f"Temperament: {self.temperament}")
         print(f"Color: {self.color}")

     def pet_name(self):
         return self.name