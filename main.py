import turtle

import numpy as np
import pandas
screen = turtle.Screen()
screen.title("U.S States game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
print(int(data["x"][data[data["state"] == "Wyoming"].index]))
guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(f"Guesses {len(guessed_states)}/50 ", prompt="whats the states name?")
    if answer.lower() == "exit":
        missing_states = []
        for state in data["state"]:
            if state not in guessed_states:
                missing_states.append(state)
        break
    for state in data["state"]:
        if answer.lower() == state.lower() and answer.lower() not in guessed_states:
            guessed_states.append(state)
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto((int(data["x"][data[data["state"] == state].index])), (int(data["y"][data[data["state"] == state].index])))
            t.write(state)

missing_states_file = pandas.DataFrame(missing_states)
missing_states_file.to_csv("States to learn.csv")
