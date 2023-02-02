from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("orange red")
screen = Screen()
screen.colormode(255)


# draw a dashed line
# for num in range(50):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# make turtle draw 3-10 sided shape with each shape a different color
# for num in range(3, 11):
#     timmy.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
#     for _ in range(num):
#         timmy.forward(100)
#         timmy.right(360/num)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# have turtle do a random walk, changing colors with each segment
# directions = [0, 90, 180, 270]
# timmy.pensize(10)
# timmy.speed("fastest")
# for num in range(200):
#     timmy.pencolor(random_color())
#     timmy.forward(20)
#     timmy.setheading(random.choice(directions))

# simulate a spirograph
timmy.speed("fastest")
def draw_sprirograph(angle):
    for _ in range(int(360 / angle)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.right(angle)

draw_sprirograph(2)

screen.exitonclick()
