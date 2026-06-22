from turtle import Turtle

from pong.constants import (
    COURT_HEIGHT,
    PADDLE_LEFT_EDGE,
    PADDLE_WIDTH,
    STRETCH_FACTOR,
)

class Paddle:
    _number_of_segments = 8
    _moving_up = False
    _moving_down = False
    # _move_delay = 0.015
    _move_distance = PADDLE_WIDTH * 2

    def __init__(self, screen):
        self.screen = screen
        # self._paddle = [
        #     Paddle._build_paddle_segment() for _ in range(Paddle._number_of_segments)
        # ]
        self._paddle = Paddle.build_paddle()

    @staticmethod
    def build_paddle():
        paddle = Turtle()
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=(Paddle._number_of_segments * STRETCH_FACTOR), stretch_len=STRETCH_FACTOR)
        paddle.penup()

        return paddle

    @staticmethod
    def _build_paddle_segment():
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.shapesize(stretch_wid=STRETCH_FACTOR, stretch_len=STRETCH_FACTOR)
        segment.penup()
        segment.speed("fastest")

        return segment

    def get_length(self):
        # return len(self._paddle) * paddle_width
        return Paddle._number_of_segments * PADDLE_WIDTH
        # return self._paddle.shapesize()[0]

    def move_to(self, x, y):
        # for index, segment in enumerate(self._paddle):
        #     segment.goto(x, y - (index * paddle_width))
        self._paddle.goto(x, y)

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
        # print("Moving paddle up")

        # if self._paddle[0].ycor() >= (COURT_HEIGHT / 2) - self._move_distance:
        if self._paddle.ycor() >= (COURT_HEIGHT / 2) - (self.get_length() / 2) - self._move_distance:
            self.stop_moving()
            return

        # for segment in self._paddle:
        #     segment.goto(segment.xcor(), segment.ycor() + self._move_distance)
        self._paddle.goto(self._paddle.xcor(), self._paddle.ycor() + self._move_distance)

        # timer.sleep(self._move_delay)

    def move_down(self):
        # print("Moving paddle down")
        # self._moving_up = False
        # self._moving_down = True

        # while (
        #     self._moving_down
        #     and self._paddle[len(self._paddle) - 1].ycor()
        #     > -(COURT_HEIGHT / 2) + paddle_width
        # ):
        #     for segment in self._paddle:
        #         segment.goto(segment.xcor(), segment.ycor() - paddle_width)

        #     self.screen.update()
        #     timer.sleep(self._move_delay)

        # print("Moving paddle down")

        if (
            # self._paddle[len(self._paddle) - 1].ycor() <= -(COURT_HEIGHT / 2) + self._move_distance
            self._paddle.ycor() <= -(COURT_HEIGHT / 2) + (self.get_length() / 2) + self._move_distance
        ):
            return

        # for segment in self._paddle:
        #     segment.goto(segment.xcor(), segment.ycor() - self._move_distance)
        self._paddle.goto(self._paddle.xcor(), self._paddle.ycor() - self._move_distance)

    def stop_moving(self):
        self._moving_up = False
        self._moving_down = False

    def get_edge(self, edge):
        paddle_x = self._get_edge_x(edge)
        length = self.get_length()
        paddle_y_range = (
            # self._paddle[0].ycor() + PADDLE_WIDTH / 2,
            # self._paddle[-1].ycor() - PADDLE_WIDTH / 2,
            self._paddle.ycor() + (length / 2),
            self._paddle.ycor() - (length / 2),
        )

        # print(f"Paddle length: {self.get_length()}, paddle_y_range: {paddle_y_range}")
        return (paddle_x, paddle_y_range)

    def _get_edge_x(self, edge):
        if PADDLE_LEFT_EDGE == edge:
            # return self._paddle[0].xcor() - (PADDLE_WIDTH / 2)
            return self._paddle.xcor() - (PADDLE_WIDTH / 2)

        # return self._paddle[0].xcor() + (PADDLE_WIDTH / 2)
        return self._paddle.xcor() + (PADDLE_WIDTH / 2)
