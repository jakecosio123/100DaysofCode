#For use with Reeborg's World Hurdle 3 (find link in the Readme)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#loop to jump over hurdles using functions defined by Reeborg's World
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#loop to decide between moving forward or jumping   
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()