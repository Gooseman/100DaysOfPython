from turtle import Turtle

from constants import COURT_DISTANCE_FROM_EDGE, GAME_HEIGHT


class Scoreboard:
    def __init__(self):
        self.left_score = 0
        self.right_score = 0
        self.score_display = Scoreboard.create_writer()

        self.update_scoreboard()

    @staticmethod
    def create_writer():
        score_display = Turtle()

        score_display.color("#66CFFF")
        score_display.hideturtle()
        score_display.pensize(5)
        score_display.penup()
        score_display.goto(0, GAME_HEIGHT / 2 - COURT_DISTANCE_FROM_EDGE)
        return score_display

    def update_scoreboard(self):
        self.score_display.clear()
        self.score_display.write(
            f"{self.left_score}    {self.right_score}",
            align="center",
            font=("Courier", 36, "normal"),
        )

    def increase_left_score(self):
        self.left_score += 1

    def increase_right_score(self):
        self.right_score += 1

    def get_scores(self):
        return self.left_score, self.right_score
