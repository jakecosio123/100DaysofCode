from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.level = 0

    def move(self):
        for num in range(len(self.cars)):
            self.cars[num].forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * self.level)

    def create_car(self):
        if random.randint(1, 3) == 3:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setx(315)
            new_car.sety(random.randint(-280, 265))
            new_car.setheading(180)
            self.cars.append(new_car)

    def new_level(self):
        self.level += 1
        for car in self.cars:
            car.hideturtle()
        self.cars = []

    def collision(self, player_xcor, player_ycor):
        for num in range(len(self.cars)):
            if self.cars[num].distance(player_xcor, player_ycor) < 25:
                return True
