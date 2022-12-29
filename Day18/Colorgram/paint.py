"""import colorgram

colors_list=[]
number_of_colors = 6
colors = colorgram.extract("a.jpg", number_of_colors)

for i in range(number_of_colors):
    next_color = colors[i]
    rgb = next_color.rgb
    color=(rgb.r,rgb.g,rgb.b)
    print(rgb)
    colors_list.append(color)

print(colors_list)"""

from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)

colors_list = [(230, 228, 224),
               (229, 223, 226),
               (217, 226, 220),
               (195, 172, 121),
               (221, 226, 231),
               (156, 97, 59)]
a=20

def row():
    for i in range(9):
        t.dot(5,random.choice(colors_list))
        t.up()
        t.fd(20)
for i in range(9):
    row()
    t.setpos(0,a)
    a+=20
t.ht() 

screen.mainloop
