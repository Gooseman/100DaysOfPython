import math
import time
from snake_segment import SnakeSegment


class Snake:
    head_colour = "white"
    body_colour = "green"

    def __init__(
        self,
        screen,
        base_segment_length,
        snake_width_factor,
        initial_segments,
        game_length,
        game_height,
    ):
        from turtle import Turtle

        self.move_delay = 0.1
        self.screen = screen

        self.base_snake_length = base_segment_length
        self.snake_width_factor = snake_width_factor
        self.snake_width = snake_width_factor * base_segment_length
        self.initial_length_factor = initial_segments

        self.head_pos = [0, 0]

        def create_segment(index):
            return SnakeSegment(
                [self.head_pos[0] - index * self.snake_width, 0],
                self.base_snake_length,
                self.snake_width_factor,
                self.head_colour if index == 0 else self.body_colour,
            )

        self.body = [create_segment(index) for index in range(0, initial_segments)]

        self.game_right = game_length / 2 - self.snake_width / 2
        self.game_left = -self.game_right
        self.game_top = game_height / 2 - self.snake_width / 2
        self.game_bottom = -self.game_top

    # Move the snake forward one segment lenght.
    # The head just moves in whatever direction it is facing.
    # each segment must then move to the previous position of the segment ahead of it.
    def move(self):
        for index, segment in enumerate(self.body):
            if 0 == index:
                segment.move_forward()
            else:
                segment.move_to(self.body[index - 1].get_last_position())

        self.screen.update()
        time.sleep(self.move_delay)

    def turn_left(self):
        self.body[0].turn_left()

    def turn_right(self):
        self.body[0].turn_right()

    def has_collided(self):
        body_positions = [segment.get_position() for segment in self.body[1:]]

        return self.body[0].will_collide(
            self.game_left,
            self.game_right,
            self.game_top,
            self.game_bottom,
            body_positions,
        )

    def grow(self):
        tail = self.body[-1]
        tail_last_pos = tail.get_last_position()

        new_segment = SnakeSegment(
            tail_last_pos,
            self.base_snake_length,
            self.snake_width_factor,
            self.body_colour,
        )

        self.body.append(new_segment)
        self.move_delay *= 0.99

    def get_snake_width(self):
        return self.snake_width

    def get_snake_positions(self):
        return [segment.get_position() for segment in self.body]

    def get_snake_mouth_position(self):
        return self.body[0].get_position()
