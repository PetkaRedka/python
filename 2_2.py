my_list = input("Enter list elemts (space-separated): ").split()

for i in range(0, len(my_list) - 1, 2):

    temp = my_list[i + 1]
    my_list[i + 1] = my_list[i]
    my_list[i] = temp

print(my_list)
    
