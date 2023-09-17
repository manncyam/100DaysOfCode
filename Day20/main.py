from turtle import Screen
import time
from snake import Snake

screen = Screen()
snake = Snake()

def setup_screen():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)    
    screen.listen()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")

def start():
    is_on = True
    while is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

def main():
    setup_screen()
    start()

    screen.exitonclick()

if __name__ == "__main__":
    main()