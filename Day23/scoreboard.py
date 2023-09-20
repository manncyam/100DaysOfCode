from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-285, y=260)
        self.level = 0
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", move=False, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER!", move=False, align="center", font=FONT)
