from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = ["t1", "t2", "t3", "t4", "t5", "t6"]
positions = [(-225, 125), (-225, 75), (-225, 25), (-225, -25), (-225, -75), (-225, -125)]


for turtle_index in range(6):
    turtles[turtle_index] = Turtle(shape="turtle")
    turtles[turtle_index].color(colors[turtle_index])
    turtles[turtle_index].penup()
    turtles[turtle_index].goto(positions[turtle_index])


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won!")
            else:
                print(f"You've lost! The {winning_color} turtle won.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
