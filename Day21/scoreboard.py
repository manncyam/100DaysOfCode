from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
Y_SCORE = 260 

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=Y_SCORE)
        self.score = 0
        self.write_score()
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", move=False, align=ALIGNMENT, font=FONT)