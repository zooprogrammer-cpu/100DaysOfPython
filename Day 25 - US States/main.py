import turtle
import pandas

screen = turtle.Screen()
screen.title("Us States game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 5:
    answer_state = screen.textinput(title = f"Guess the State {len(guessed_states)}/50", prompt= "Provide a state name.").title()

    if answer_state == 'Exit':
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

        guessed_states.append(answer_state)

# not_guessed_states = []

# for state in all_states:
#     if state not in guessed_states:
#         not_guessed_states.append(state)

not_guessed_states = [state for state in all_states if state not in guessed_states]

print(not_guessed_states)

data_dict = {
    "states" : not_guessed_states
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("states_to_learn.csv")
