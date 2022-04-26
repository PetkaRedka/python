def summator3000():

    sum = 0
    while(1):
    
        print("Enter 'Q' for exit!")

        my_list = input("Enter numbers (or smth else): ").split()
        for i in range(len(my_list)):

            if my_list[i].isdigit():
                sum += float(my_list[i])
            
            elif my_list[i].upper() == 'Q':
                return sum

        print(sum)

print(summator3000())



