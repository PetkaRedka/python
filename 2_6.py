product_list = []

while(1):

    print("\nMenu:\n" +
          "1) Add new product\n" + 
          "2) Show products analitic\n" +
          "3) Exit\n")

    menu_number = input("Enter a menu number: ")
    
    if (menu_number < '1' or menu_number > '3'):
        print("Number has to be 1, 2 or 3!")
    
    # Добавление нового элемента
    elif (menu_number == '1'):
        
        product_list.append( 
        (
            len(product_list) + 1, 
            {
                "name": input("Enter new product name: "), 
                "cost": float(input("Enter new product cost: ")), 
                "amount": int(input("Enter new product amount: ")), 
                "units": input("Enter new product units: ")
            }
        ))

        print("\nStructure:")
        for i in product_list:
            print(i)

    # Вывод аналитики
    elif (menu_number == '2'):

        analitic = {
            "name": [],
            "cost": [],
            "amount": [],
            "units": []
        }

        for i in range(len(product_list)):
            for j in product_list[i][1].keys():

                if product_list[i][1][j] not in analitic[j]:
                    analitic[j].append(product_list[i][1][j])

        print("Current analitic:")
        for i in analitic.items():
            print(i)
    
    # Опция Exit
    else:

        print("Exit!")
        break