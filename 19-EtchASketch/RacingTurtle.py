from turtle import Turtle

class RacingTurtle:
    def __init__(self, name, colour):
        self.turtle = Turtle(shape="turtle")

        self.turtle.color(colour)
        self.turtle.penup()
        self.turtle.goto(-200, 0)
        self.turtle.pendown()
        self.name = name

    def set_postion(self, x, y, heading=0):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(heading)
        self.turtle.pendown()

    def get_position(self):
        return self.turtle.xcor()

    def move_forward(self, distance):
        self.turtle.forward(distance)
