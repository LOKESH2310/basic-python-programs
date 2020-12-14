num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2nd number : "))

def get_gcd(num1 , num2):
    while num2 :
        num1 , num2 = num2 , num1 % num2
    return num1

print("GCD of two numbers :" ,get_gcd(num1 , num2))