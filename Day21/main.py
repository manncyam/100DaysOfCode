from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

def setup_screen():
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.title("Snake Game")
    screen.tracer(0)    
    screen.listen()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")

def is_collide_wall():
    h = snake.head
    x = h.xcor()
    y = h.ycor()
    return x > 290 or x < -290 or y < -290 or y > 290

def start():
    is_on = True
    while is_on:
        screen.update()
        time.sleep(0.2)
        snake.move()

        if snake.is_collide_with_food(food):
            snake.extend_segments()
            food.refresh()
            scoreboard.update_score()
        if snake.is_hitting_body() or is_collide_wall():
            is_on = False
            scoreboard.game_over()
        
def main():
    setup_screen()
    start()


    screen.exitonclick()

if __name__ == "__main__":
    main()