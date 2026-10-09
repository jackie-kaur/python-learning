import user

class ATM:
    users = [] 
    startingMoney = 0

    def __init__(self, startingMoney):
        self.startingMoney = startingMoney

    def deposit(self, user, money):
        for u in self.users:
            if user == u.name():
                u.deposit(money)
                self.startingMoney = self.startingMoney + money

    def is_valid_user(self, name):
        for u in self.users:
            if name == u.name():
                return True
        return False

    def withdraw(self, user, money):
        for u in self.users:
            if user == u.name():
                u.withdraw(money)
                self.startingMoney = self.startingMoney - money

    def checkBalance(self, user):
        for u in self.users:
            if user == u.name():
                return u.balance()

    def is_user_able_to_transact(self, user):
        for u in self.users:
            if user == u.name():
                return u.is_able_to_transact()
        return False

    def has_enough_money(self, asked_money):
        if asked_money < self.startingMoney:
            return True
        return False

    def add_user(self, name, money):
        u = user.User(name, money)
        self.users.append(u)

    def atm_deposit(self, money):
        self.startingMoney = self.startingMoney + money