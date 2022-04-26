# Через **
def my_func1(x, y):
    
    try:
        return round(float(x) ** int(y), 4) if float(x) >= 0 \
             and int(y) < 0 else "Wrong arguments!" 
    
    except ValueError as err:
        return err

# Через цикл
def my_func2(x, y):

    sum = 1

    try:
        y = int(y)
        x = float(x)
        
    except ValueError as err:
        return err

    if x >= 0 and y < 0:
        for i in range(abs(y)):
            sum /= x
        
        return round(sum, 4)
    
    else:
        return "Wrong arguments!"


x = input("Enter x: ")
y = input("Enter y: ")

print(f"1st variant: {my_func1(x, y)} \n" + 
      f"2nd variant: {my_func2(x, y)}")