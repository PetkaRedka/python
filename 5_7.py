from json import dump

with open("file_7.txt", "r", encoding="utf-8") as my_file:
    
    average_profit = []
    profit_dict = {}

    for line in my_file.readlines():
        
        name, form, profit, ne_profit = line.split()
        value = float(profit) - float(ne_profit)
        if value > 0: 
            average_profit.append(value)
    
        profit_dict[name] = float(profit) - float(ne_profit)
    
    json_list = [profit_dict, {"average_profit": sum(average_profit) / len(average_profit)}]

    with open("json_7.json", "w", encoding="utf-8") as json_file:
        dump(json_list, json_file, ensure_ascii=False, indent=4)