def get_gcd(num1 , num2):
    while num2 :
        num1 , num2 = num2 , num1 % num2
    return num1


numbers = []
get =  int(input("ENTER THE NUMBER OF ELEMENT TO BE ADDED :"))
for i in range(0 , get):
    add = int(input())
    numbers.append(add)
gcd = get_gcd(numbers[0], numbers[1])
for i in range(2, len(numbers)):
    gcd = get_gcd(gcd, numbers[i])

print(gcd)