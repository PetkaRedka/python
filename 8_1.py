class Date():

    def __init__(self, date):
        
        self.date = date
        Date.parser(date)


    
    @classmethod
    def parser(cls, date):

        try:
            day, month, year = map(int, date.split("-"))

        except ValueError:
            print("Формат ввода должен быть дд-мм-гггг")
            return

        cls.checker(day, month, year)  
        
    @staticmethod
    def checker(day, month, year):
        
        day_dict = {31: [1, 3, 5, 7, 8, 10, 12], 30: [4, 6, 9, 11], 28: [2]}
        
        if year < 0:
            print("Год должен быть >= 0!")
            return

        if 1 <= month <= 12 and 1 <= day <= 31:

            for key, value in day_dict.items():
                if month in value and day <= key:
                    
                    print("Дата введена корректно!")
                    return
            
            print("В этом месяце нет такого количества дней!")

        else:
            print("Месяц должен быть в передалах от 1 до 12, а день от 1 до 31")


d = Date("20-12-2012")
d = Date("40-00-1")
d = Date("dd-mm-yyyy")
d = Date("30-02-2012")