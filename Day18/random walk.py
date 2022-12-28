from turtle import Turtle, Screen
from random import randint, choice

my_turtle = Turtle()
my_turtle.speed(10)
my_turtle.pensize(10)
screen = Screen()
screen.colormode(255)
def random_walk():
    choice = randint(0, 2)
    if choice == 1:
        my_turtle.left(90)
    elif choice == 2:
        my_turtle.right(90)
    else:
        my_turtle.fd(40)

while True:
    my_turtle.color(randint(0,255), randint(0,255), randint(0,255))
    random_walk()


screen.exitonclick()