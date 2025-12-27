from turtle import Turtle


class Scoreboard:
    def __init__(self, game_height):
        self.score = 0
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.color("white")
        self.pen.penup()
        self.pen.goto(0, game_height / 2 - 40)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.pen.clear()
        self.pen.write(
            f"Score: {self.score}", align="center", font=("Arial", 24, "normal")
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.update_scoreboard()

    def declare_game_over(self):
        self.pen.goto(0, 0)
        self.pen.color("red")
        self.pen.write("GAME OVER", align="center", font=("Arial", 36, "bold"))
