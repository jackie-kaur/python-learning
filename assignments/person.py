class Person:

    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def school(self):
        if self.age < 18 and self.age > 0 :
            print(f"{self.name} is {self.age} years old and goes to school.")
        elif self.age == 18:
            print(f"It is {self.name}'s last year of school!")
        elif self.age > 18:
            print(f"{self.name} graduated school.")
        else:
            print(f"Invalid age for {self.name}!")

p1 = Person("Zöe", 23) 
p1.school()

p2 = Person("Singh", -34)
p2.school()