raiting_list = [7, 5, 3, 3, 2]
raiting_elem = int(input("Enter a new rainting element: "))

if (raiting_list[-1] >= raiting_elem):
    raiting_list.append(raiting_elem)

else:

    for i in range(-1, (len(raiting_list) - 1)):

        if (raiting_elem > raiting_list[i + 1]):

            raiting_list.insert(i + 1, raiting_elem)
            break

print(raiting_list)