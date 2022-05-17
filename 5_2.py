with open("file_2.txt", "r", encoding="utf-8") as my_file:
    
    text = my_file.readlines()
    for i in range(len(text)):
        print(f"{i + 1}) {len(text[i].split())}")
