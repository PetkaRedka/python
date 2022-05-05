from itertools import count, cycle
from socket import NI_NUMERICHOST

# Итератор, генерирующий целые числа, начиная с указанного
while(1):
    
    try: 
        number = count(int(input("Enter the number: ")))
        break
    
    except ValueError:
        print("It has to be number!")

my_list = list(next(number) for i in range(10))
print("Count:", my_list) 

# итератор, повторяющий элементы некоторого списка, определённого заранее
number = cycle(my_list)
print("Cycle:", [next(number) for i in range(len(my_list) * 3)])

