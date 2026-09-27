print("===========================\nWelcome to the calculator.\n===========================")

def add(a, b):
    total = a + b
    print(f"{total} is your answer.")

def sub(c, d):
    diff = c - d
    print(f"{diff} is your answer.")
  
def mult(e, f):
    prod = e * f
    print(f"{prod} is your answer.")
  
def div(g, h):
    if h == 0:  
        print("Error: Division by zero is not allowed.")
        return
    quo = g // h
    print(f"{quo} is your answer.")

def power(i, j):
    ans = i ** j
    print(f"{ans} is your answer.")

while True:
    choose = input(" 1 for add\n 2 for sub\n 3 for mult\n 4 for div\n 5 for exponents\n 'exit' for Exit\n Choice: ")
    if choose == "exit":
        break

    if choose not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice. Please try again.")
        continue
    
    a = float(input("Choose 1st number."))
    b = float(input("Choose 2nd number."))

    if choose == "1":
        add(a, b)
    elif choose == "2":
        sub(a, b)
    elif choose == "3":
        mult(a, b)
    elif choose == "4":
        div(a, b)
    elif choose == "5":
        power(a, b)
    else:
        print("Invalid choice. Please try again.")