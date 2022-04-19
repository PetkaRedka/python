a = float(input("Enter the fisrt day distance: " ))
b = float(input("Enter a max distance: "))
day_number = 1


while (a < b):

    a *= 1.1
    day_number += 1

print(day_number)