from turtle import Turtle, Screen
from random import randint, choice

my_turtle = Turtle()
my_turtle.speed(0)
screen = Screen()
screen.colormode(255)

def randomColor():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_colour = (r, g, b)
    return random_colour

for i in range(0, 360, 10):
    my_turtle.setheading(i)
    my_turtle.circle(100)
    my_turtle.color(randomColor())


screen.exitonclick()