import turtle
import pandas as pd

#Screen Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Game components
data = pd.read_csv("50_states.csv")
correct_guesses = 0
game_on = True
guessed_answers = []
missing_states = []

## Turtle writer
writer = turtle.Turtle()
writer.penup()
writer.color("black")
writer.hideturtle()


while game_on:
    answer = screen.textinput(f"{correct_guesses}/50 Guessed", "What's another state name?")
    for states in data["state"]:
        if (
                answer.lower() == states.lower() and
                answer not in guessed_answers
        ):
            x_pos = int(data[data["state"] == states]["x"].iloc[0])
            y_pos = int(data[data["state"] == states]["y"].iloc[0])
            # Alternative:
            # state_data = data[data.state == answer]
            # x_pos = state_data.x.item()
            # y_pos = state_data.y.item()
            writer.goto(x=x_pos, y=y_pos)
            writer.write(
                arg=f"{states}",
                move=False,
                align="center",
                font=("Courier", 8, "bold")
            )
            correct_guesses += 1
            guessed_answers.append(states.lower())

    if correct_guesses == 50 or answer == 'exit':
        game_on = False

for states in data["state"]:
    if states.lower() not in guessed_answers:
        missing_states.append(states)

states_to_learn = pd.DataFrame({
    "Missing States": missing_states
})
states_to_learn.to_csv("states_to_learn.csv")

screen.exitonclick()