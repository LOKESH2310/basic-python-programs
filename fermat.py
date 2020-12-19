
def get_input():
    a = int(input("Enter (a): "))
    b = int(input("Enter (b): "))
    c = int(input("Enter (c): "))
    n = int(input("Enter (n): "))
    return check_fermat(a, b, c, n)

def check_fermat(a, b, c, n):
    if n > 2 and (a ** n + b ** n == c ** n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")

get_input()

