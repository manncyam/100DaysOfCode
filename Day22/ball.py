from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self, screen: Screen):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("darkorange")
        self.seth(37)
        self._screen = screen
        self.move_speed = 0.1

    def move(self):
        self.forward(10)

    def refresh(self):
        self.seth(-self.heading())
        self.move_speed = 0.1
        self.goto(0,0)
    
    def bounce_x(self):
        self.move_speed *= 0.9
        self.seth(180 - self.heading())

    def bounce_y(self):
        self.seth(-self.heading())