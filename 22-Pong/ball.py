from turtle import Turtle


class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.speed(0)

    def move(self):
        self.ball.forward(10)

    def reset_position(self):
        self.ball.goto(0, 0)
        # self.ball.dx *= -1

    def get_position(self):
        return self.ball.xcor(), self.ball.ycor()

    def set_heading(self, heading):
        self.ball.setheading(heading)

    def bounce_y(self):
        pass
