from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_clockwise():
    tim.right(10)


def turn_counterclockwise():
    tim.left(10)


def clear_screen():
    tim.home()
    tim.clear()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=turn_clockwise)
screen.onkeypress(key="d", fun=turn_counterclockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()