print("Welcome to the calculator.")

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
    quo = g // h
    print(f"{quo} is your answer.")

def power(i, j):
    ans = i ** j
    print(f"{ans} is your answer.")

while True:
    choose = input("1 for add, 2 for sub, 3 for mult, 4 for div, 5 for exponents, 'exit' for Exit")
    if choose == "exit":
        break
    
    a = int(input("Choose 1st number."))
    b = int(input("Choose 2nd number."))

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