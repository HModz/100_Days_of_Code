from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.fd(10)
    def move_down(self):
        if self.ycor()<-280:
            pass
        else:
            self.bk(10)

    def lvl_up(self):
        self.goto(STARTING_POSITION)
