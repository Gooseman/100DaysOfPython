from turtle import Turtle

from constants import COURT_HEIGHT, COURT_WIDTH


class Court:
    def __init__(self):
        self.court_lines = Turtle()
        self.court_lines.color("white")
        self.court_lines.hideturtle()
        self.court_lines.penup()
        self.draw_border()
        # self.draw_center_line()

    def draw_border(self):
        self.court_lines.goto(
            (-COURT_WIDTH / 2),
            (COURT_HEIGHT / 2),
        )
        self.court_lines.pensize(1)
        self.court_lines.pendown()

        for _ in range(2):
            self.court_lines.forward(COURT_WIDTH)
            self.court_lines.right(90)
            self.court_lines.forward(COURT_HEIGHT)
            self.court_lines.right(90)

        self.court_lines.penup()

    def draw_center_line(self):
        dash_length = 15
        line_length = COURT_HEIGHT - dash_length * 2

        self.court_lines.goto(0, -line_length / 2)
        self.court_lines.setheading(90)
        # self.court_lines.pensize(5)
        self.court_lines.pendown()

        for _ in range(line_length // (dash_length * 2) + 1):
            self.court_lines.forward(dash_length)
            self.court_lines.penup()
            self.court_lines.forward(dash_length)
            self.court_lines.pendown()
