# combine3
number = int(input("Enter the number : "))
check = number
sum = 0
reverse = 0
while check >0 :
    numbers = check % 10
    sum = sum + numbers
    check = check // 10
    reverse = reverse*10 + numbers
if reverse == number :
    print ("It is a palindrome number")
else :
    print ("It is not a palindrome number")
print("Sum of the number : " ,sum)
print("Reverse of the number : " ,reverse)
