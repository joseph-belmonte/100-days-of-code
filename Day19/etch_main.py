""" this module is for the main file of the etch-a-sketch project """
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    """move the turtle forward by 10 paces"""
    tim.forward(10)


def move_backwards():
    """move the turtle backwards by 10 paces"""
    tim.backward(10)


def turn_left():
    """turn the turtle left by 10 degrees"""
    tim.left(10)


def turn_right():
    """turn the turtle right by 10 degrees"""
    tim.right(10)


def clear():
    """clear the screen"""
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
# on key listener from python docs
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=turn_right)
screen.onkey(key="d", fun=move_backwards)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

# going to bind wasd keys to move the turtle around
