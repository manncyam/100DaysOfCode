from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.seth(90)
        self.restart()

    def restart(self):
        self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])

    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def reach_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y