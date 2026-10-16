# The login could be for admin or user. Admin can add a user and deposit money in ATM. User should be able to withdraw, deposit, balance

import atm as a

def admin_loop(atm):
    num_of_choice = 0
    while True:
        print("\n1. Add User")
        print("2. Deposit ATM Money")
        print("3. Exit")
        print("")

        admin_ask = int(input("Choice:"))

        if admin_ask == 1:
            user = input("What is your name: ")
            money = int(input("How much money do you have: "))
            print(f"New user added:\n\
                    Name: {user}\n\
                    Money: {money}")
            atm.add_user(user, money)
        elif admin_ask == 2:
            money = int(input("How much money do you want to deposit to the ATM: "))
            print("Money Deposited.")
            atm.atm_deposit(money)
        elif admin_ask == 3:
            print("Logged Out.")
            return
        else:
            print("Invalid Number.")

def user_loop(atm):
    user = input("What is your name: ")
    while True:
        print("\n1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Current Balance")
        print("4. Exit")
        print("")

        user_ask = int(input("Choice:"))

        if user_ask == 1:
            if not atm.is_user_able_to_transact(user):
                print("You are out of transactions for the day.")
                continue

            money = int(input("How much money do you want to deposit: "))
            atm.deposit(user, money)
            print("Money Deposited.")
        elif user_ask == 2:
            if not atm.is_user_able_to_transact(user):
                print("You are out of transactions for the day.")
                continue
            number_withdraw = int(input("How much money you want to withdraw: "))
            if not atm.has_enough_money(number_withdraw):
                print("Sorry, ATM does not have that much money to withdraw.")
                continue
            balance = atm.checkBalance(user)
            if number_withdraw > balance:
                print("You cannot withdraw because your balane is less than the withdraw amount.")
                continue
            
            atm.withdraw(user,number_withdraw)
            print("Money Withdrawn.")
        elif user_ask == 3:
            balance = atm.checkBalance(user)
            print("Your balance is: " , balance)
        elif user_ask == 4:
            print("Logged Out.")
            return
        else:
            print("Invalid Number.")

def which_loop(atm):
    while True:
        print("\n Login as: ")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        print("")

        ask_choice = int(input("Choice:"))

        if ask_choice == 1:
            admin_loop(atm)
        elif ask_choice == 2:
            user_loop(atm)
        elif ask_choice == 3:
            print("Logging Out.")
            return
        else:
            print("Invalid.")


def main():

    atm = a.ATM(1000)

    print("******************")
    print("WELCOME TO THE ATM")
    print("******************\n")

    which_loop(atm)

main()