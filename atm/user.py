# This class holds money and name of a user
class User:
    name_ = ""
    money_ = 0
    t_count_ = 0

    def __init__(self, name, money):
        self.name_ = name
        self.money_ = money

    # Returns balance of the user
    def balance(self):
        return self.money_

    def withdraw(self, withdrawMoney):
        self.t_count_ = self.t_count_ + 1
        self.money_ = self.money_ - withdrawMoney

    def deposit(self, depositMoney):
        self.t_count_ = self.t_count_ + 1
        self.money_ = self.money_ + depositMoney

    def name(self):
        return self.name_

    def is_able_to_transact(self):
        if self.t_count_ < 3:
            return True
        return False