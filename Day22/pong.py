from scoreboard import ScoreBoard

from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_OFFSET = 50

class Pong:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.setup_screen()
        self.ball = Ball(self.screen)
        self.scoreboard = ScoreBoard()
        self.left_paddle = Paddle((-(SCREEN_WIDTH / 2 - PADDLE_OFFSET), 0))
        self.right_paddle = Paddle((SCREEN_WIDTH / 2 - PADDLE_OFFSET, 0))
        self.register_paddle()

    def setup_screen(self):
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)

    def register_paddle(self):
        self.screen.listen()
       
        self.screen.onkeypress(fun=self.left_paddle.up, key="w")
        self.screen.onkeypress(fun=self.left_paddle.down, key="s")
        
        self.screen.onkeypress(fun=self.right_paddle.up, key="Up")
        self.screen.onkeypress(fun=self.right_paddle.down, key="Down")

    def is_hit_paddle(self):
        # ball x is within paddle length
        return (self.ball.distance(self.left_paddle) < 50 and self.ball.xcor() - self.left_paddle.xcor() < 25)\
              or (self.ball.distance(self.right_paddle) < 50 and self.right_paddle.xcor() - self.ball.xcor() < 25)
        # ball y is within 12
        
    def is_hit_wall(self):
        return self.ball.ycor() > 285 or self.ball.ycor() < -285

    def is_missed(self):
        return self.is_missed_on_right() or self.is_missed_on_left()
    
    def is_missed_on_right(self):
        #increase left score
        if self.ball.xcor() > 370:
            self.scoreboard.increase_left_score()
            return True
        return False
    
    def is_missed_on_left(self):
        #increase right score
        if self.ball.xcor() < -370:
            self.scoreboard.increase_right_score()
            return True
        return False
    
    def start(self):
        is_on = True
        pause_checking = False
        count = 0
        while is_on:
            self.screen.update()
            time.sleep(self.ball.move_speed)
            if self.is_missed():
                self.scoreboard.update_score()
                time.sleep(.5)
                self.ball.refresh()
            else:    
                if self.is_hit_paddle() and not pause_checking:
                    self.ball.bounce_x()
                    pause_checking = True
                    count = 0
                elif self.is_hit_wall():
                    self.ball.bounce_y()
                if count > 5:
                    pause_checking = False
                count += 1


            self.ball.move()
            