#For use with Reeborgs World Maze (find link in the Readme)
#defines function to enable turning right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#loops until Reeborg reaches the goal
while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and not right_is_clear():
        turn_left()
    elif right_is_clear():
        turn_right()
        move()