class Cell:

    def __init__(self, n):
        self.__n = n

    def __add__(self, cell):
        return Cell(self.__n + cell.__n)

    def __sub__(self, cell):

        sub_ = self.__n - cell.__n
        if sub_ > 0:
            return Cell(sub_)
        else:
            print("Нельзя применить операцию вычитания")
    
    def __mul__(self, cell):
        return Cell(self.__n * cell.__n)

    def __truediv__(self, cell):
        return Cell(self.__n // cell.__n)
    
    def make_order(self, n_raw):

        for i in range(self.__n // n_raw):
            print(n_raw * "*")
        print((self.__n % n_raw) * "*")
    
    def __str__(self):
        return (f"Number: {self.__n}")

cell1 = Cell(11)
cell1.make_order(5)

cell2 = Cell(4)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
