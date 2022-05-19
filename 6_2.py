class Road:

    def __init__(self, length, width):
        
        self._length = length
        self._width = width

    def find_mass(self, mass = 25, thickness = 5):
        print(f"{self._width}m * {self._length}m * {mass}kg * {thickness}sm = " \
            f"{(self._width * self._length * mass * thickness) / 1000}t")


road = Road(float(input("Enter the road length: ")), float(input("Enter the road width: ")))
road.find_mass()