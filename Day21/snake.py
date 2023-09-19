from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180
COLLISION_DISTANCE = 15 

class Snake:

    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]

    def creat_snake(self):
        for i in range(3):
            self.segments.append(self.creat_new_segment(-i * 20, 0))
        
    def move(self):
        for n in range(len(self.segments) -1, 0, -1):
            self.segments[n].goto(self.segments[n-1].xcor(), self.segments[n-1].ycor())
    
        self.head.forward(MOVE_DISTANCE)

    def creat_new_segment(self, at_x, at_y):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.up()
        segment.goto(x=at_x, y=at_y)
        return segment
    
    def is_hitting_body(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True

        return False
    
    def extend_segments(self):
        segment = self.creat_new_segment(self.segments[len(self.segments) - 1].xcor(), self.segments[len(self.segments) - 1].ycor())
        self.segments.append(segment)
        if len(self.segments) > 10:
            for s in self.segments:
                s.color("lightgreen")

    def is_collide_with_food(self, food):
        return self.head.distance(food) < COLLISION_DISTANCE 
    
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