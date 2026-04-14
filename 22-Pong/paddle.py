import time as timer
from turtle import Turtle

from constants import (
    court_height,
    paddle_left_edge,
    paddle_right_edge,
    paddle_width,
    stretch_factor,
)


class Paddle:
    _number_of_segments = 8
    _moving_up = False
    _moving_down = False
    _move_delay = 0.015
    _move_distance = paddle_width

    def __init__(self, screen):
        self.screen = screen
        self._paddle = [
            Paddle._build_paddle_segment() for _ in range(Paddle._number_of_segments)
        ]

    @staticmethod
    def _build_paddle_segment():
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.shapesize(stretch_wid=stretch_factor, stretch_len=stretch_factor)
        segment.penup()
        segment.speed("fastest")

        return segment

    def get_length(self):
        return len(self._paddle) * paddle_width

    def move_to(self, x, y):
        for index, segment in enumerate(self._paddle):
            segment.goto(x, y - (index * paddle_width))

    def move(self):
        # if (not self._moving_up) and (not self._moving_down):
        #     return

        if self._moving_up:
            self.move_up()

        if self._moving_down:
            self.move_down()

    def turn_up(self):
        self._moving_down = False
        self._moving_up = True

    def turn_down(self):
        self._moving_up = False
        self._moving_down = True

    def move_up(self):
        print("Moving paddle up")

        if self._paddle[0].ycor() >= (court_height / 2) - self._move_distance:
            self.stop_moving()
            return

        for segment in self._paddle:
            segment.goto(segment.xcor(), segment.ycor() + self._move_distance)

        # timer.sleep(self._move_delay)

    def move_down(self):
        # print("Moving paddle down")
        # self._moving_up = False
        # self._moving_down = True

        # while (
        #     self._moving_down
        #     and self._paddle[len(self._paddle) - 1].ycor()
        #     > -(court_height / 2) + paddle_width
        # ):
        #     for segment in self._paddle:
        #         segment.goto(segment.xcor(), segment.ycor() - paddle_width)

        #     self.screen.update()
        #     timer.sleep(self._move_delay)

        print("Moving paddle down")

        if (
            self._paddle[len(self._paddle) - 1].ycor()
            <= -(court_height / 2) + self._move_distance
        ):
            return

        for segment in self._paddle:
            segment.goto(segment.xcor(), segment.ycor() - self._move_distance)

    def stop_moving(self):
        self._moving_up = False
        self._moving_down = False

    def get_edge(self, edge):
        paddle_x = self._get_edge_x(edge)
        paddle_y_range = (
            self._paddle[0].ycor() + paddle_width / 2,
            self._paddle[-1].ycor() - paddle_width / 2,
        )

        return (paddle_x, paddle_y_range)

    def _get_edge_x(self, edge):
        if paddle_left_edge == edge:
            return self._paddle[0].xcor() - (paddle_width / 2)

        return self._paddle[0].xcor() + (paddle_width / 2)
