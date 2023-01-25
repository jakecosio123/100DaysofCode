import turtle
import pandas
from state_writer import StateWriter

df = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_writer = StateWriter()
score = 0
guessed_states = []
all_states = df.state.to_list()
print(all_states)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Guessed", prompt="What's another state's name").title()
    if answer_state in df.state.unique() and answer_state not in guessed_states:
        guessed_state = df[df.state == answer_state]
        state_writer.write_state(int(guessed_state.x), int(guessed_state.y), answer_state)
        guessed_states.append(answer_state)
        score += 1
    elif answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


turtle.mainloop()



