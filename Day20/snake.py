from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]

    def creat_snake(self):
        for i in range(3):
            t = Turtle(shape="square")
            t.color("white")
            t.up()
            t.goto(x=-i*20, y=0)
            self.segments.append(t)
        
    def move(self):
        for n in range(len(self.segments) -1, 0, -1):
            self.segments[n].goto(self.segments[n-1].xcor(), self.segments[n-1].ycor())
    
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)