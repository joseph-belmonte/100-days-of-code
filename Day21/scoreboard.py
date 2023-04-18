""" This will handle the food logic for the snake game."""
import random
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class scoreboard(Turtle):
    """Creates the scoreboard class"""

    # init will get called every time we create a new instance of the class
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """ Ends the game"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
