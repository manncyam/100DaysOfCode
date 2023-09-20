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
        self.high_score = 0
        self.read_high_score()
        self.write_score()
        
    def update_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score: 
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.write_score()
         
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", move=False, align=ALIGNMENT, font=FONT)

    def write_high_score(self):
        with open("data.txt", mode="w") as f:
            f.write(f("{self.high_score}"))

    def read_high_score(self):
        with open("data.txt") as f:
            self.high_score = int(f.read())