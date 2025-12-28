import math
import random
import time

from ball import Ball
from constants import (
    court_height,
    court_width,
    paddle_distance_from_edge,
    paddle_left_edge,
    paddle_right_edge,
)
from court import Court
from paddle import Paddle
from scoreboard import Scoreboard


class Game:
    _game_on = False

    def __init__(self, screen):
        self.screen = screen
        self.court = Game._create_court()
        self.scoreboard = Scoreboard()
        self.left_paddle, self.right_paddle = self._create_paddles()
        print(self.left_paddle, self.right_paddle)
        self.ball = Game._create_ball()
        self.max_ball_angle = Game._get_max_ball_angle()

        screen.update()

        self.screen.listen()
        self.screen.onkey(
            lambda: self._handle_paddle_move(self.left_paddle.turn_up), "w"
        )
        self.screen.onkey(
            lambda: self._handle_paddle_move(self.left_paddle.turn_down), "s"
        )
        self.screen.onkey(
            lambda: self._handle_paddle_move(self.right_paddle.turn_up), "Up"
        )
        self.screen.onkey(
            lambda: self._handle_paddle_move(self.right_paddle.turn_down), "Down"
        )
        self.screen.onkey(lambda: self.right_paddle.stop_moving(), "Left")
        self.screen.onkey(lambda: self.right_paddle.stop_moving(), "Right")
        self.screen.onkey(lambda: self.left_paddle.stop_moving(), "a")
        self.screen.onkey(lambda: self.left_paddle.stop_moving(), "d")
        self.screen.onkey(self.start_game, "space")

    @staticmethod
    def _create_court():
        return Court()

    def _create_paddles(self):
        left_paddle = self._create_paddle(-court_width / 2 + paddle_distance_from_edge)
        right_paddle = self._create_paddle(court_width / 2 - paddle_distance_from_edge)

        return left_paddle, right_paddle

    def _create_paddle(self, x_position):
        paddle = Paddle(self.screen)
        paddle_length = paddle.get_length()

        paddle.move_to(x_position, 0 + (paddle_length / 2))
        return paddle

    @staticmethod
    def _create_ball():
        ball = Ball()

        ball.reset_position()
        return ball

    @staticmethod
    def _get_max_ball_angle():
        adjacent = court_width / 2
        opposite = court_height / 2

        return math.degrees(math.atan(opposite / adjacent))

    def _handle_paddle_move(self, paddle_move):
        paddle_move()
        self.screen.update()

    def start_game(self):
        print("Starting game...")
        move_count = 0
        self.ball.set_heading(random.randint(0, int(self.max_ball_angle)))
        self._game_on = True

        while self._game_on:  # and move_count < 100:
            print("Step")
            self.ball.move()
            self.left_paddle.move()
            self.right_paddle.move()

            right_paddle_edge_x, right_paddle_edge_y = self.right_paddle.get_edge(
                paddle_left_edge
            )

            if self.ball.get_position()[0] >= right_paddle_edge_x:
                print("Ball reached right paddle edge at x =", right_paddle_edge_x)

            if (
                self.ball.get_position()[1] >= right_paddle_edge_y[0]
                or self.ball.get_position()[1] <= right_paddle_edge_y[1]
            ):
                print("Ball within right paddle y range:", right_paddle_edge_y)

            self.screen.update()
            move_count += 1
            time.sleep(0.02)
        pass
