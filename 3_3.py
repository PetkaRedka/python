def my_func(a, b, c):
    
    try:
        my_list = [float(a), float(b), float(c)]
        
    except ValueError as err:
        return err
    
    min_elem = min(my_list)
    my_list.remove(min_elem)
    
    return sum(my_list)
    

print(my_func(
    input("Enter a first number: "),
    input("Enter a second number: "),
    input("Enter a third number: ")
))