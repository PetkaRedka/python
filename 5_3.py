with open("file_3.txt", "r", encoding="utf-8") as my_file:
    text_dict = {text.split()[0]: float(text.split()[1]) for text in my_file.readlines()}

sum = 0
for name, value in text_dict.items():

    if value < 20000:
        print(name)
    sum += value    
        
print("Средняя величина дохода сотрудника: %.2f" % (sum / len(text_dict.values())))
