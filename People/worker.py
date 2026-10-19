import person

class Worker(person.Person):
    job_ = ""
    dollarsPerHour_ = 0.0

    def __init__(self, name, age, job, dollarsPerHour):
        super().__init__(name, age)
        self.job_ = job
        self.dollarsPerHour_ = dollarsPerHour

    def cost_to_hire(self, hours):
        return self.dollarsPerHour_ * hours