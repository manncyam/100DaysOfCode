from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

turtle_colors = ["red", "orange", "purple", "blue", "green", "lightgreen"]
turtles = []

def create_turtle():
    space = screen.canvheight // len(turtle_colors)
    offset = screen.canvheight // 2
    count = 0
    starting_point = -(screen.canvwidth // 2)
    for c in turtle_colors:
        t = Turtle(shape="turtle")
        t.speed("slow")
        t.color(c)
        t.penup()
        t.goto(x=starting_point + t.shapesize()[0], y=space * count - offset)
        count += 1
        turtles.append(t)

def check_winner(user_input, winner):
    if user_input == winner:
        print(f"You win! The {winner} turtle is the winner.")
    else:
        print(f"You Lose! the {winner} turtle is the winner")

def start_racing(user_input):
    is_race_on = True
    goal = screen.canvwidth // 2
    while is_race_on:
        for t in turtles:
            t.forward(random.randint(-2, 10))
            if t.xcor() > goal:
                is_race_on = False
                winner = t
                break
    check_winner(user_input, winner.pencolor())

def get_user_input():
    user_input = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color {turtle_colors}: ").lower()
    return user_input

def main():
    user_input = get_user_input()
    create_turtle()
    start_racing(user_input)
    screen.exitonclick()

if __name__ == "__main__":
    main()