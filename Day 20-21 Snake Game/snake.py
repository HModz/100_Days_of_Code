from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
    def create_snake(self):
        for i in STARTING_POSITIONS:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.up()
            snake.setpos(i)
            self.snake_segments.append(snake)

    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[i - 1].xcor()
            new_y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(x=new_x, y=new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)