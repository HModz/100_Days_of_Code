from turtle import Turtle, Screen
import random

race_on = False

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle win? Enter a color:")
colors=["red", "orange", "yellow", "green", "blue", "purple"]
start_distance = -100
turtles = []

for i in range(len(colors)):
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(colors[i])
    my_turtle.up()
    my_turtle.setpos(x=-230,y=start_distance)
    start_distance+=40
    turtles.append(my_turtle)

if bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            if winner==bet:
                print("Your turtle win")
            else:
                print("Your turtle lose")
        rand_distance = random.randint(0,10)
        turtle.fd(rand_distance)

screen.exitonclick()