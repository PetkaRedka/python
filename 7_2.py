from abc import ABC, abstractmethod

class  Clothes(ABC):

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.__size = size

    @property
    def consumption(self):

        if self.__size > 0:
            return (self.__size / 6.5 + 0.5)
        
        print("Неподходящее значение!")
        return -1

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

class Costume(Coat):

    def __init__(self, height):
        self.__height = height

    @property
    def consumption(self):

        if self.__height > 0:
            return (2 * self.__height + 0.3)
        
        print("Неподходящее значение!")
        return -1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

coat = Coat(-3)
print(coat.consumption)
coat.size = 30
print(coat.consumption)

costume = Costume(-3)
print(costume.consumption)
costume.height = 1.5
print(costume.consumption)

