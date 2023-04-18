""" This will handle the food logic for the snake game."""
import random
from turtle import Turtle


class Food(Turtle):
    """Creates the food class"""

    # init will get called every time we create a new instance of the class
    def __init__(self):
        super().__init__()
        self.food = Turtle(shape="circle")
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        """Refreshes the food"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
