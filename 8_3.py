class IsStrException(Exception):

    def __init__(self, text):
        self.text = text


list = []

while((elem := input()) != "stop"):

    try:
        if elem[1::].replace(".", "", 1).isnumeric() and elem[0].replace("-", "1").isnumeric():
                list.append(round(float(elem), 2))

        else:
            raise IsStrException("Вы ввели не число!")
    
    except IsStrException as e:
        print(e)

print(list)