import person as p

class Student(p.Person):
    school_ = ""
    grade_map_ = {
        4 : "Pre-K",
        5 : "Kindergarten",
        6 : "1st Grade",
        7 : "2nd Grade",
        8 : "3rd Grade",
        9 : "4th Grade",
        10 : "5th Grade",
        11 : "6th Grade",
        12 : "7th Grade",
        13 : "8th Grade",
        14 : "10th Grade",
        16 : "11th Grade",
        17 : "12th Grade"
    }

    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school_ = school
        

    def what_division(self):
        if self.age_ <= 10:
            print(f"{self.name_} is a lower schooler ")
        elif self.age_ <= 13:
            print(f"{self.name_} is a middle schooler")
        elif self.age_ <= 17:
            print(f"{self.name_} is a high scholer")
        else:
            print(f"{self.name_} is an adult.")

    def what_grade(self):
        if self.age_ < 4:
            print(f"{self.name_} is still an infant!")

        elif self.age_ > 17:
            print(f"{self.name_} is an adult!")

        return self.grade_map_[self.age_]