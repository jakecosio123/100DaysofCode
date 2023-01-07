#For use with Reeborg's World Hurdle 4
#defines function to enable turning right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#defines jump function
def jump():
    turn_left()
    #allows Reeborg to jump the correct height
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    #allows Reeborg to get back to the ground
    while front_is_clear():
        move()
    turn_left()

#loop to decide between moving forward or jumping    
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()