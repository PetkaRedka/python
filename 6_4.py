class Car:

    def __init__(self, speed, color, name, is_police):

        self._speed = int(speed)
        self._color = color
        self._name = name
        self._is_police = is_police

        self._position = {"X": 0, "Y": 0}
        self._direction = "front"

    def go(self):
        
        # Разгоняемся
        self._speed += 10

        if self._direction == "front":
            self._position["Y"] += self._speed / 10
        elif self._direction == "back":
            self._position["Y"] -= self._speed / 10
        elif self._direction == "right":
            self._position["X"] += self._speed / 10
        elif self._direction == "left":
            self._position["X"] -= self._speed / 10

        print("Current position - X: %d Y: %d" % (self._position["X"], self._position["Y"]))
        print(f"Direction: {self._direction}")

    def stop(self):
        self._speed = 0
        print("The car was stopped")
    
    def turn(self, direction):

        if self._direction != direction:
            
            # Сбрасываем скорость на повороте
            self._speed //= 2
            self._direction = direction
            print(f"Direction was changed to '{direction}'")
        
        else:
            print("That's the same direction")

    def show_speed(self):
        print(f"Current speed: {self._speed}")


class TownCar(Car):

    def show_speed(self):

        if self._speed > 60:
            print("Speed limit exceeded (60)! Get out of the car!")
            self._speed = 0
        else:
            print(f"Current speed: {self._speed}")

class WorkCar(Car):

    def show_speed(self):

        if self._speed > 40:
            print("Speed limit exceeded (40)! Get out of the car!")
            self._speed = 0
        else:
            print(f"Current speed: {self._speed}")


class SportCar(Car):

    def turbo(self):
        if self._speed < 100:
            print("TURBO IS ON!!!")
            self._speed += 150

class PoliceCar(Car):

    def check_car(self):

        if self._is_police == False:
            print("You are imposter!")
        else:
            print("Good day, officer!")

print("---------------------- CAR -------------------")
usual_car  = Car(50, "blue", "Daisy", False)
usual_car.go()
usual_car.turn("right")
usual_car.go()
usual_car.show_speed()

print("---------------------- TOWN CAR -------------------")
town_car = TownCar(55, "red", "BMV", False)
town_car.go()
town_car.show_speed()
town_car.show_speed()

print("---------------------- WORK CAR -------------------")
work_car = TownCar(20, "red", "BMV", False)
town_car.stop()
town_car.show_speed()

print("---------------------- SPORT CAR -------------------")
sport_car = SportCar(200, "fire", "Flash", False)
sport_car.go()
sport_car.turn("left")
sport_car.turn("front")
sport_car.go()
sport_car.turbo()
sport_car.go()
sport_car.show_speed()

print("---------------------- POLICE CAR -------------------")
police_car = PoliceCar(50, "blue", "929023", True)
police_car.check_car()
police_car._is_police = False
police_car.check_car()





    

    



