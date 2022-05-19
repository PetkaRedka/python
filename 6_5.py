class Stationery:

    def __init__(self, title):
        self._title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):

    def draw(self):
        print(f"Я ручка по имени {self._title}!")

class Pencil(Stationery):

    def draw(self):
        print(f"Я карандаш по имени {self._title}!")

class Handle(Stationery):

    def draw(self):
        print(f"Я маркер по имени {self._title}!")

st = Stationery("pen")
st.draw()
pen = Pen("Ира")
pen.draw()
pencil = Pencil("Иван")
pencil.draw()
handle = Handle("Георг")
handle.draw()

