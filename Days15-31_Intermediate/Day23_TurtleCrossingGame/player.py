from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green4")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(10)

    def new_level(self):
        self.goto(STARTING_POSITION)
