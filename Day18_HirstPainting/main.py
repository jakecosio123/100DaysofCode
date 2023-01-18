# import colorgram
import turtle as t
import random

# used to extract the color palette from the Hirstspotpainting.jpg
# colors = colorgram.extract('Hirstspotpainting.jpg', 30)
# color_palette = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_palette.append(new_color)
#
# print(color_palette)

palette = [
    (144, 76, 50), (188, 165, 117), (166, 153, 36), (14, 46, 85), (139, 185, 176),
    (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169),
    (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172),
    (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71),
    (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)
]
# initial set up - change color mode, make turtle object,
# make it not leave a path and move fast while invisible, set start position
t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()
tim.setpos(-250, -250)

# draw dots every 50 px. After 10 dots, move up a line and repeat
for num in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(palette))
        tim.forward(50)
    if num < 9:
        tim.setpos(-250, tim.ycor()+50)

screen = t.Screen()
screen.exitonclick()
