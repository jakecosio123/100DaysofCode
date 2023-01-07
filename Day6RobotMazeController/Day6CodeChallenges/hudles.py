#for use at Reeborg's World: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

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