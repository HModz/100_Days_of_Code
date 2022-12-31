from turtle import Turtle


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pu()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center")

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center")

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center")