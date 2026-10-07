import animal

class Agency:
    pets = []

    def display_pets(self):
        print("The Avaliable Pets:\n")
        for p in self.pets:
            if not p.is_adopted():
                p.info()
                print("")

    def adopt_pet(self, name, adopted_by):
        for p in self.pets:
            if p.pet_name() == name:
                p.adopt(adopted_by)

    # Adds a new pet in the list
    def add_pet(self, name, age, sex, type, temperament, color):
        a = animal.Animal(name, age, sex, type, temperament, color)
        self.pets.append(a)

    def is_present(self, name):
        for p in self.pets:
            if name == p.pet_name() and p.is_adopted() == False:
                return True
        return False