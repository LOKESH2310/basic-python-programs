num = int(input("ENTER THE NUMBER : "))
x = num / 2
x1 = x * x
while x1 != x :
    x = x1
    x1 = ( x + num / x ) / 2
print("THE SQUARE ROOT OF THE GIVEN NUMBER IS : " ,x1)