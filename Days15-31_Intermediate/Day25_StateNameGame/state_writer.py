import turtle
FONT = ("Courier", 8, "normal")

class StateWriter(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")

    def write_state(self,x_cor, y_cor, state_name):
        self.goto(x_cor, y_cor)
        self.write(arg=state_name, align="center", font=FONT)
