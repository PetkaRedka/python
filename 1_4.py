num = int(input("Enter your number: "))
max_digit = 0

while (num > 0):

    if max_digit < num % 10:
        max_digit = num % 10
    
    if (max_digit == 9):
        break
    else:
        num //= 10

print("Max digit: ", max_digit)