from turtle import Turtle

from high_score import HighScore

class Scoreboard:
    def __init__(self, game_height):
        self.score = 0
        self._game_height = game_height
        self.pen = Turtle()
        self.pen.hideturtle()
        self._set_score_pen()
        self.high_score = HighScore()
        self._update_scoreboard()

    def _set_score_pen(self):
        self.pen.color("white")
        self.pen.penup()
        self.pen.goto(0, self._game_height / 2 - 40)

    def _update_scoreboard(self):
        self.pen.clear()

        score_line = f"Score: {self.score}\tHigh Score: {self.high_score.high_score}"

        self.pen.write(score_line, align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self._update_scoreboard()

    def reset(self):
        self.high_score.update_high_score(self.score)
        self.score = 0
        self._set_score_pen()
        self._update_scoreboard()

    def declare_game_over(self):
        self.pen.goto(0, 0)
        self.pen.color("red")
        self.pen.write("GAME OVER", align="center", font=("Arial", 36, "bold"))
