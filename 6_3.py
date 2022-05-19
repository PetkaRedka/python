class Worker:

    def __init__(self, name, surname, position, wage, bonus):

        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    
    def get_full_name(self):
        print(f"Full name: {self.surname} {self.name}")
    
    def get_total_income(self):

        if self._income["wage"].isdigit() and self._income["bonus"].isdigit():
            print(f"Total income: {sum(map(float, self._income.values()))}")
        
        else:
            print("Wrong numbers!")
    
position = Position(
    input("Enter your name: "),
    input("Enter your surname: "),
    input("Enter your position: "),
    input("Enter your wage: "),
    input("Enter your bonus: "),
)
position.get_full_name()
position.get_total_income()