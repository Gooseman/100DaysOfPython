from turtle import Turtle

class Ball:
    _move_distance = 10
    _forward = 1
    _backward = -1
    _direction = _forward

    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.speed(0)
        self._move_distance = self.get_width() / 2

    def move(self):
        self.ball.forward(self._move_distance)

    def reset_position(self):
        self.ball.goto(0, 0)
        self._direction = self._forward
        # self.ball.dx *= -1

    def get_position(self):
        return self.ball.xcor(), self.ball.ycor()
    
    def get_width(self):
        return self.ball.shapesize()[0] * 20

    def set_heading(self, heading):
        self.ball.setheading(heading)

    def bounce_y(self):
        print("Bouncing ball vertically. Current heading:", self.ball.heading())
        self.set_heading((-self.ball.heading()) % 360)

    def bounce_x(self):
        print("Bouncing ball. Current heading:", self.ball.heading())
        self.set_heading((180 - self.ball.heading()) % 360)
        self._direction *= -1

    def is_moving_right(self):
        return self._direction == self._forward
    
    def is_moving_left(self):
        return self._direction == self._backward
