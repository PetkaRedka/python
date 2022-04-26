def division(a, b):
    
    try:
        return (float(a) / float(b))
    
    except ValueError as err:
        return err

    except ZeroDivisionError:
        return "Don't try to divide by zero!"


print(division(
    input("Enter a first number: "),
    input("Enter a second number: ")
))