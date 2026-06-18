from random import choice
from turtle import Turtle

# For some reason, pylint on github is unable to find these values in the constants module.
# pylint: disable=no-name-in-module
from constants import BASE_SQUARE_SIZE, CAR_COLOURS, CAR_LENGTH_FACTORS

class Car(Turtle):
    def __init__(self, position, speed):
        super().__init__()
        self.shape("square")
        self.color(choice(CAR_COLOURS))
        self.penup()
        self.goto(position)
        self.speed = speed
        self.length = choice(CAR_LENGTH_FACTORS)
        self.shapesize(stretch_wid=0.5, stretch_len=self.length)

    def move(self):
        self.backward(self.speed)

    def get_right_edge(self):
        return self.xcor() + ((BASE_SQUARE_SIZE / 2) * self.length)

    def get_left_edge(self):
        return self.xcor() - ((BASE_SQUARE_SIZE / 2) * self.length)

    def has_collided_with(self, frog_right_edge):
        # print(f"Checking collision: Car left edge = {self.get_left_edge()}, Frog right edge = {frog_right_edge}")
        return self.get_left_edge() <= frog_right_edge and self.get_right_edge() >= frog_right_edge - BASE_SQUARE_SIZE
