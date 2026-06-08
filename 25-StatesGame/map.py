
from turtle import Turtle, Screen

class Map(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.screen = Screen()
        self.screen.title("25 States Game")
        self.screen.setup(width=725, height=491)
        self.screen.bgpic("blank_states_img.gif")

    def display_state(self, state_name, x, y):
        self.goto(x, y)
        self.write(state_name, align="center", font=("Arial", 10, "normal"))