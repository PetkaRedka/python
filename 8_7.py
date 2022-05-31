from msilib.schema import CompLocator


class ComplexNumber():

    def __init__(self, number, complex):

        self.number = number
        self.complex = complex
    
    def __add__(self, other):
        return ComplexNumber(self.number + other.number,
                                self.complex + other.complex)

    def __mul__(self, other):
        return ComplexNumber(self.number * other.number - self.complex * other.complex,
                                self.number * other.complex + self.complex * other.number)
    
    def __str__(self):

        if self.complex > 0:
            return f"{self.number}+{self.complex}i"
        else:
            return f"{self.number}{self.complex}i"       


a = ComplexNumber(3, 2)
b = ComplexNumber(1, 7)

print(a + b)
print(a * b)