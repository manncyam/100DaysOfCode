import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move, key="Up")

def squize():
    for car in car_manager.cars:
        if abs(player.ycor() - car.ycor()) < 20 and abs(car.xcor() - player.xcor()) < 15:
            return True
    return False

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    if player.reach_finish_line():
        player.restart()
        scoreboard.update_level()
        car_manager.create_cars(2)
    if squize():
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()