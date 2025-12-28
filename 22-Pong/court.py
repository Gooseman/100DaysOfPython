from turtle import Turtle

from constants import court_distance_from_edge, court_height, court_width


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
            (-court_width / 2),
            (court_height / 2),
        )
        self.court_lines.pensize(1)
        self.court_lines.pendown()

        for _ in range(2):
            self.court_lines.forward(court_width)
            self.court_lines.right(90)
            self.court_lines.forward(court_height)
            self.court_lines.right(90)

        self.court_lines.penup()

    def draw_center_line(self):
        dash_length = 15
        line_length = court_height - dash_length * 2

        self.court_lines.goto(0, -line_length / 2)
        self.court_lines.setheading(90)
        # self.court_lines.pensize(5)
        self.court_lines.pendown()

        for _ in range(line_length // (dash_length * 2) + 1):
            self.court_lines.forward(dash_length)
            self.court_lines.penup()
            self.court_lines.forward(dash_length)
            self.court_lines.pendown()
