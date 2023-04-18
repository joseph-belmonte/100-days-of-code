"""Creates the snake class"""
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    """Creates the snake class"""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the snake body"""
        starting_positions = STARTING_POSITIONS
        for position in starting_positions:
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position)
            self.segments.append(new_turtle)

    def add_segment(self):
        """Adds a segment to the snake"""
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(self.segments[-1].position())
        self.segments.append(new_turtle)

    def extend(self):
        """Extends the snake"""
        self.add_segment()

    def move(self):
        """Moves the snake"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Moves the snake up"""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """Moves the snake down"""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        """Moves the snake left"""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """Moves the snake right"""
        if self.head.heading() != 180:
            self.head.setheading(0)
