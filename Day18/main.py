from turtle import Turtle, Screen
import random
import colorgram

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

def get_color_list():
    rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    
    return rgb_colors

def random_color():
    return random.choice(color_list)

def create_hirst_painting(t:Turtle, width, height, dot_size, gap):
    origin = t.position()
    for i in range(width):
        t.setpos(origin[0], origin[1] + i * gap)
        for _ in range(height):
            t.dot(dot_size, random_color())
            t.forward(gap)

def main():
    screen = Screen()
    screen.colormode(255)
    timmy = Turtle()
    timmy.speed('fastest')
    timmy.penup()
    timmy.goto((-screen.canvwidth // 2, -screen.canvheight // 2))
    timmy.hideturtle()
    create_hirst_painting(timmy, 10, 10, 15, 50)
    screen.exitonclick()

if __name__ == "__main__":
    main()