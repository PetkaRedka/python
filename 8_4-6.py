class StorageOverflow(Exception):

    def __init__(self, text):
        self.text = text


class Storage:
    
    inventarisation_dict = {"printers": 0, "scanners": 0, "xeroxes": 0}

    def __init__(self, free_volume=1000):
        self.free_volume = free_volume


    def menu(self):

        print("\nВведите номер операции:\n" +
                "1) Завезти новую партию оргтехники на склад\n" +
                "2) Забрать часть техники со склады на нужды IT-отдела\n" +
                "3) Провести инвенторизацию\n"
                "4) Выход\n")

        while((elem := input("Номер: ")) != "4"):
            
            try:
                if elem == "1":
                    self.equip_reception(
                        int(input("Количество принтеров в новой партии:")),
                        int(input("Количество сканеров:")),
                        int(input("Количество ксероксов:"))
                        )

                elif elem == "2":
                    self.take_from_storage(
                        int(input("Количество принтеров которые необходимо забрать:")),
                        int(input("Количество сканеров:")),
                        int(input("Количество ксероксов:"))
                    )

                elif elem == "3":
                    self.enventarization()
                
                else:
                    print("Неправильный номер команды")

            except ValueError:
                print("Неправильный формат ввода!")
                

    def equip_reception(self, printer_count = 0, scaner_count = 0, xerox_count = 0):
        
        if (printer_count < 0 or scaner_count < 0 or xerox_count < 0):
            print("Неправильный формат ввода!")
            return

        sum_volume = printer_count * Printer.get_volume() + \
                        scaner_count * Scaner.get_volume() + \
                            xerox_count * Xerox.get_volume()
        
        try:
            if self.free_volume - sum_volume < 0:
                raise StorageOverflow("Склад переполнен, операция отменена!")
        
        except StorageOverflow as e:
            print(e)
        
        else:

            self.inventarisation_dict["printers"] += printer_count
            self.inventarisation_dict["scanners"] += scaner_count
            self.inventarisation_dict["xeroxes"] += xerox_count

            self.free_volume -= sum_volume
            print(f"На складе осталось {self.free_volume} свободного места")


    def take_from_storage(self, printer_count = 0, scaner_count = 0, xerox_count = 0):
        
        if (printer_count < 0 or scaner_count < 0 or xerox_count < 0):
            print("Неправильный формат ввода!")
            return

        if printer_count > self.inventarisation_dict["printers"]:
            print("На складе нет столько принтеров! Операция не будет выполнена!")
            return

        if scaner_count > self.inventarisation_dict["scanners"]:
            print("На складе нет столько сканеров! Операция не будет выполнена!")
            return

        if xerox_count > self.inventarisation_dict["xeroxes"]:
            print("На складе нет столько ксероксов! Операция не будет выполнена!")
            return   

        sum_volume = printer_count * Printer.get_volume() + \
                        scaner_count * Scaner.get_volume() + \
                            xerox_count * Xerox.get_volume()
        
        
        self.free_volume += sum_volume
        print(f"На складе теперь {self.free_volume} свободного места")
        
    def enventarization(self):

        print("\nСейчас на складе:\n" +
                "Принтеров: %d\n" % self.inventarisation_dict["printers"] +
                "Сканеров: %d\n" % self.inventarisation_dict["scanners"] +
                "Ксероксов: %d\n" % self.inventarisation_dict["xeroxes"])
    

class Office_Equipment():
    
    @classmethod
    def get_volume(cls):
        return cls.volume

class Printer(Office_Equipment):
    volume = 2

class Scaner(Office_Equipment):
    volume = 1
    
class Xerox(Office_Equipment):
    volume=4

s = Storage()
s.menu()