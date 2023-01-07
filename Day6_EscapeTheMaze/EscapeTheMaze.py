#For use with Reeborgs World Maze (find link in the Readme)
#defines function to enable turning right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#set loop variable to check if stuck in a loop
loop = 0
#loops until Reeborg reaches the goal
while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
        loop = 0
    elif wall_in_front() and not right_is_clear():
        turn_left()
        loop = 0
    #if we do the following 4 times we are stuck in a loop, incrementing the loop variable each time will force it out of the loop by sending it to the else statement
    elif right_is_clear() and loop < 4:
        turn_right()
        move()
        loop += 1
    else:
        move()
        loop = 0