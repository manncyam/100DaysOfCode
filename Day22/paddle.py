from turtle import Turtle

MOVE_STEP = 20

class Paddle(Turtle):
    
    def __init__(self, xy):
        super().__init__()
        self.setup_paddle(xy)

    def setup_paddle(self, xy):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=xy[0], y=xy[1])
            
    def up(self):
        if self.ycor() < 240:
            self.goto(x=self.xcor(), y= self.ycor() + MOVE_STEP)

    def down(self):
        if self.ycor() > -240:
            self.goto(x=self.xcor(), y= self.ycor() - MOVE_STEP)