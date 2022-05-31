import sys

class CheckNull(ZeroDivisionError):

    def __init__(self, text):
        self.text = text


try:
    a = 20
    b = int(input())
    
    if b == 0:
        raise CheckNull("Успел до ZeroDivisionError!")

except CheckNull as e:
    print(e)

except (ZeroDivisionError, ValueError) as e:
    print(e)
    sys.exit(1)

else:
    print("Все окей!")

print("Продолжаем работу")