tranclate_dict = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

with open("file_4.txt", "r", encoding="utf-8") as eng_file:
    with open("file_4_rus.txt", "w", encoding="utf-8") as rus_file:
        
        text = eng_file.read()
        for eng_number, rus_number in tranclate_dict.items():
            text = text.replace(eng_number, rus_number)

        rus_file.write(text)
    