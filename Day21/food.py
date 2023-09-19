from turtle import Turtle
import random

X_MIN = -280
X_MAX = 280
Y_MIN = -280
Y_MAX = 280

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(X_MIN, X_MAX)
        random_y = random.randint(Y_MIN, Y_MAX)
        self.goto(x=random_x, y=random_y)