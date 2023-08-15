# Imports
from turtle import Turtle, Screen
import random

# Objects
myScreen = Screen()
color = ["red", "orange", "yellow", "blue", "pink", "green"]
y_pos = [-80, -40, 0, 40, 80, 120]
all_turtle = []

# Main Program
myScreen.setup(height=400, width=500)
bet = myScreen.textinput("Make a bet", "Which turtle will win the race?")

for t in range(0, 6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.penup()
    newTurtle.goto(x=-230, y=y_pos[t])
    newTurtle.color(color[t])
    all_turtle.append(newTurtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == bet:
                print(f"You've Won! The winning color is {win_color}")
            else:
                print(f"You've Lost! The winning color is {win_color}")
        distance = random.randint(0, 10)
        turtle.forward(distance)


myScreen.exitonclick()

