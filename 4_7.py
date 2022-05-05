def factorial(n):
    
    if n == 0:
        return 1
    
    return n * factorial(n - 1)

def fact(n):
     
     for i in range(1, n + 1):
         yield  factorial(i)

while(1):

    try:
        n = int(input("Enter your number: "))

        if n <= 0:
            print("Number has to be bigger than 0!")
        else:
            break
    
    except ValueError:
        print("It has to be a number!")

for el in fact(n):
    print(el)
