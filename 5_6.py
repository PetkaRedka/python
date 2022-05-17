with open("file_6.txt", "r", encoding="utf-8") as my_file:

    my_dict = { 
                text.split(":")[0]: \
                sum(map(int, text.split(":")[1].replace("(пр)", "") \
                    .replace("(лаб)", "").replace("(л)", "") \
                    .replace("-", "0").split())) \
                for text in my_file.readlines()
              }
    print(my_dict)