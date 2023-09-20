import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POSITIONS = [x for x in range(-240, 240, 20)]
START_X = 400

class Car(Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.penup()
        self.color(color)
        self.seth(180)

class CarManager():
    
    def __init__(self):
        self.cars = []
        self.create_cars(10)
        self.place_cars()

    def create_cars(self, num):
        for _ in range(num):
            car = Car(random.choice(COLORS))
            self.cars.append(car)

    def place_cars(self):
        for car in self.cars:
            self.place_car_at_starting_point(car, START_X, random.choice(Y_POSITIONS))

    def place_car_at_starting_point(self, car: Turtle, x, y):
        car.goto(x=x, y=y)

    def move_cars(self):
        for car in self.cars:
            move_distance = STARTING_MOVE_DISTANCE
            if random.choice([True, False]):
                move_distance += MOVE_INCREMENT

            car.forward(move_distance)
            if car.xcor() < -350:
                self.place_car_at_starting_point(car, START_X, random.choice(Y_POSITIONS))