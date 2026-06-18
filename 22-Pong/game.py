import math
import random
import time

from ball import Ball
from constants import (
    PADDLE_LEFT_EDGE,
    PADDLE_RIGHT_EDGE,
    COURT_HEIGHT,
    COURT_WIDTH,
    PADDLE_DISTANCE_FROM_EDGE,
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
            lambda: self._handle_paddle_move(self.left_paddle.turn_up, self.left_paddle.move), "w"
        )
        self.screen.onkey(
            lambda: self._handle_paddle_move(self.left_paddle.turn_down, self.left_paddle.move), "s"
        )
        self.screen.onkey(
            lambda: self._handle_paddle_move(self.right_paddle.turn_up, self.right_paddle.move), "Up"
        )
        self.screen.onkey(
            lambda: self._handle_paddle_move(self.right_paddle.turn_down, self.right_paddle.move), "Down"
        )
        self.screen.onkey(self.right_paddle.stop_moving, "Left")
        self.screen.onkey(self.right_paddle.stop_moving, "Right")
        self.screen.onkey(self.left_paddle.stop_moving, "a")
        self.screen.onkey(self.left_paddle.stop_moving, "d")
        self.screen.onkey(self.start_game, "space")

    @staticmethod
    def _create_court():
        return Court()

    def _create_paddles(self):
        left_paddle = self._create_paddle(self._left_paddle_x_pos())
        right_paddle = self._create_paddle(self._right_paddle_x_pos())

        return left_paddle, right_paddle

    def _left_paddle_x_pos(self):
        return -COURT_WIDTH / 2 + PADDLE_DISTANCE_FROM_EDGE

    def _right_paddle_x_pos(self):
        return COURT_WIDTH / 2 - PADDLE_DISTANCE_FROM_EDGE

    def _create_paddle(self, x_position):
        paddle = Paddle(self.screen)

        self._reset_paddle_position(paddle, x_position)
        return paddle

    def _reset_paddle_position(self, paddle, x_position):
        # paddle.move_to(x_position, 0 + (paddle.get_length() / 2))
        paddle.move_to(x_position, 0)
        paddle.stop_moving()

    @staticmethod
    def _create_ball():
        ball = Ball()

        ball.reset_position()
        return ball

    @staticmethod
    def _get_max_ball_angle():
        adjacent = COURT_WIDTH / 2
        opposite = COURT_HEIGHT / 2

        return math.degrees(math.atan(opposite / adjacent))

    def _handle_paddle_move(self, paddle_direction, paddle_move):
        if not self._game_on:
            return

        paddle_direction()
        paddle_move()
        # self.screen.update()

    def start_game(self):
        if self._game_on:
            return

        print("Starting game...")
        move_count = 0
        self.ball.set_heading(random.randint(0, int(self.max_ball_angle)))
        self._game_on = True

        while self._game_on:  # and move_count < 100:
            # print("Step")
            self.ball.move()
            # self.left_paddle.move()
            # self.right_paddle.move()

            if self.ball.is_moving_right():
                self._handle_rightward_move()
            else:
                self._handle_leftward_move()

            self.screen.update()
            move_count += 1
            time.sleep(0.05)

    def _handle_rightward_move(self):
        # Investigate using the Turtle distance method to determine if the ball is within range of the paddle, rathe
        # than calculating the edges and ranges ourselves.
        ball_position_x, ball_position_y = self.ball.get_position()
        ball_width = self.ball.get_width()

        if self._has_hit_top_or_bottom_wall(ball_position_y, ball_width):
            self.ball.bounce_y()

        right_paddle_edge_x, right_paddle_edge_y = self.right_paddle.get_edge(PADDLE_LEFT_EDGE)
        is_past_right_paddle = (ball_position_x - ball_width) >= right_paddle_edge_x

        # print(f"Ball position: ({ball_position_x}, {ball_position_y}), right_paddle_edge_x: {right_paddle_edge_x}
        # is_past_right_paddle: {is_past_right_paddle}")

        if is_past_right_paddle:
            self._handle_ball_pasted_right_paddle()

        ball_at_right_paddle_edge = \
            (ball_position_x - ball_width / 2) <= right_paddle_edge_x <= (ball_position_x + ball_width / 2)
        ball_within_right_paddle_y_range = right_paddle_edge_y[0] >= ball_position_y >= right_paddle_edge_y[1]

        if (ball_at_right_paddle_edge and ball_within_right_paddle_y_range):
            # print("Ball within right paddle y range:", right_paddle_edge_y)
            # print("Ball at right paddle edge:", right_paddle_edge_x)
            self.ball.bounce_x()

    def _has_hit_top_or_bottom_wall(self, ball_position_y, ball_width):
        has_hit_top_wall = (ball_position_y + ball_width / 2) >= (COURT_HEIGHT / 2)
        has_hit_bottom_wall = (ball_position_y - ball_width / 2) <= -(COURT_HEIGHT / 2)

        return has_hit_top_wall or has_hit_bottom_wall

    def _handle_ball_pasted_right_paddle(self):
        # print("Ball passed right paddle edge at x =", right_paddle_edge_x)
        self._game_on = False
        self.ball.reset_position()
        self._reset_paddle_position(self.right_paddle, self._right_paddle_x_pos())
        self._reset_paddle_position(self.left_paddle, self._left_paddle_x_pos())

    def _handle_leftward_move(self):
        ball_position_x, ball_position_y = self.ball.get_position()
        ball_width = self.ball.get_width()

        if self._has_hit_top_or_bottom_wall(ball_position_y, ball_width):
            self.ball.bounce_y()

        left_paddle_edge_x, left_paddle_edge_y = self.left_paddle.get_edge(PADDLE_RIGHT_EDGE)
        is_past_left_paddle = (ball_position_x + ball_width) <= left_paddle_edge_x

        if is_past_left_paddle:
            self._handle_ball_pasted_left_paddle()

        ball_at_left_paddle_edge = \
            (ball_position_x - ball_width / 2) <= left_paddle_edge_x <= (ball_position_x + ball_width / 2)
        ball_within_left_paddle_y_range = left_paddle_edge_y[0] >= ball_position_y >= left_paddle_edge_y[1]

        if (ball_at_left_paddle_edge and ball_within_left_paddle_y_range):
            # print("Ball within left paddle y range:", left_paddle_edge_y)
            # print("Ball at left paddle edge:", left_paddle_edge_x)
            self.ball.bounce_x()

    def _handle_ball_pasted_left_paddle(self):
        # print("Ball reached left paddle edge at x =", left_paddle_edge_x)
        self._game_on = False
        self.ball.reset_position()
        self._reset_paddle_position(self.right_paddle, self._right_paddle_x_pos())
        self._reset_paddle_position(self.left_paddle, self._left_paddle_x_pos())
