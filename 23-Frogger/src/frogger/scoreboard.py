from turtle import Turtle

from frogger.constants import GAME_HEIGHT, GAME_WIDTH

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.reset()

    def update_scoreboard(self):
        self.clear()
        self.goto(-GAME_WIDTH / 2 + 30, GAME_HEIGHT / 2 - 20)
        self.write(f"Level: {self.level}", align="center", font=("Arial", 12, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 36, "bold"))

    def reset(self):
        self.level = 1
        self.update_scoreboard()
