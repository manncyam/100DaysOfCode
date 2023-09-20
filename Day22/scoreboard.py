from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
Y_SCORE = 200 

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=Y_SCORE)
        self.left_score = 0
        self.right_score = 0
        self.write_score()
        
    def update_score(self):
        self.clear()
        self.write_score()

    def increase_right_score(self):
        self.right_score += 1
    
    def increase_left_score(self):
        self.left_score += 1

    def write_score(self):
        self.write(f"{self.left_score} | {self.right_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", move=False, align=ALIGNMENT, font=FONT)