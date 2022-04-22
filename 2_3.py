
while(1):

    month = int(input("Enter a month number: "))

    if month < 1 or month > 12:
        print("The number has to be between 1 and 12!")
    
    else:
        break
    

# Реализация через список
season_list = ["winter", "winter", "spring",
              "spring", "spring", "summer",
              "summer", "summer", "autumn", 
              "autumn", "autumn", "winter"]

print(season_list[month - 1])

# Реализация через словарь
season_dict = { 1: "winter", 2: "winter", 3: "spring",
                4: "spring", 5: "spring", 6: "summer",
                7: "summer", 8: "summer", 9: "autumn",
                10: "autumn", 11: "autumn", 12: "winter"}

print(season_dict[month])