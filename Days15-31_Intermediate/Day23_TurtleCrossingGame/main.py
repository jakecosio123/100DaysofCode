import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    car_manager.move()
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()

    # detect collision with car
    if car_manager.collision(player.xcor(), player.ycor()):
        scoreboard.game_over()
        game_is_on = False

    # detect beating the level
    if player.ycor() > 270:
        scoreboard.level_up()
        car_manager.new_level()
        player.new_level()

screen.exitonclick()
