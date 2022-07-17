from pickle import TRUE
import turtle
from numpy import False_
import pandas
from tkinter import messagebox

PROMPT_TEXT = "Take a guess on the state name"
guessed_states = []
close_game = False


###############
# Setup Screen
###############
screen = turtle.Screen()
screen.title("U.S States Game")

################################################
# Read state names and cordinates from CSV file
################################################
states = pandas.read_csv("50_states.csv")

###########################################
# Add new Image as a shape to turtle shapes
###########################################
image = "blank_states_img.gif"
screen.addshape(image)

###################################
# Assign turtle with created shape
###################################
turtle.shape(image)


########################
# Let's loop the input #
########################
while len(guessed_states) < 50:
    take_a_guess_input = screen.textinput(title="Guess the state", prompt=PROMPT_TEXT).title()
    all_states = states.state.to_list()

    if take_a_guess_input == "quit":
        break
    elif take_a_guess_input in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == take_a_guess_input]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        PROMPT_TEXT = "Good Job! Guess another one!"
        guessed_states.append(state_data.state.item())
    elif take_a_guess_input not in all_states:
        PROMPT_TEXT = "Wrong guess! Try Again."
    


screen.exitonclick()