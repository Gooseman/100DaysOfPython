from random import choice
from turtle import Turtle

from constants import base_square_size, car_colours, car_length_factors

class Car(Turtle):
    def __init__(self, position, speed):
        super().__init__()
        self.shape("square")
        self.color(choice(car_colours))
        self.penup()
        self.goto(position)
        self.speed = speed
        self.length = choice(car_length_factors)
        self.shapesize(stretch_wid=0.5, stretch_len=self.length)
    
    def move(self):
        self.backward(self.speed)
    
    def get_right_edge(self):
        return self.xcor() + ((base_square_size / 2) * self.length)

    def get_left_edge(self):
        return self.xcor() - ((base_square_size / 2) * self.length)

    def has_collided_with(self, frog_right_edge):
        # print(f"Checking collision: Car left edge = {self.get_left_edge()}, Frog right edge = {frog_right_edge}")
        return self.get_left_edge() <= frog_right_edge and self.get_right_edge() >= frog_right_edge - base_square_size
    