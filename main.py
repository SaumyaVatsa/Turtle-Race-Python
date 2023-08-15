# Imports
from turtle import Turtle, Screen

# Objects
tim = Turtle()
myScreen = Screen()


# Functions
def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


# Main Program
myScreen.listen()
myScreen.onkey(key="w", fun=move_forward)
myScreen.onkey(key="s", fun=move_backward)
myScreen.onkey(key="a", fun=turn_left)
myScreen.onkey(key="d", fun=turn_right)


myScreen.exitonclick()

