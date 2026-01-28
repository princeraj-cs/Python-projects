import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_state = data.state.to_list()
guest_states = []

while len(guest_states) < 50 :
    answer_state = screen.textinput(title=f"{len(guest_states)}/50 States Correct",
                                    prompt="Whats another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in all_state:
        guest_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


# States to remember.csv
learn_state = []
for state in all_state:
    if state not in guest_states:
        learn_state.append(state)

state_dict = {
    "states": learn_state
}

df = pd.DataFrame(state_dict)
df.to_csv("remember.csv")

