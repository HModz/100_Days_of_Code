from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT)
