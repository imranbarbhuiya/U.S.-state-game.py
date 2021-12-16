import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(f"{len(guessed_states)}/{len(all_states)} state guessed", "What's the another "
                                                                                              "state name'?").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)

states_to_learn = list(set(all_states) - set(guessed_states))
# print(f"You guessed {len(guessed_states)} states")
# print(f"You need to learn {len(states_to_learn)} states")
# print(states_to_learn)

new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")
