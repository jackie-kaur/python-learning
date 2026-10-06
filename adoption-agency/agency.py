import animal

class Agency:
    pets = []

    def display_pets(self):
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