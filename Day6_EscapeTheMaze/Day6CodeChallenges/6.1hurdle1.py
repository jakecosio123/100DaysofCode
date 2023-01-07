#For use with Reeborg's World Hurdle 1 (find link in the Readme)

#define function to turn right with less lines of code
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
#loop to jump over 6 hurdles
for num in range(0,6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()