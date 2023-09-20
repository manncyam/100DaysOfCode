from pong import Pong
from turtle import Screen

def main():
    screen = Screen()

    pong = Pong(screen)
    pong.start()

    screen.exitonclick()
if __name__ == "__main__":
    main()