import math
import time
from snake_segment import SnakeSegment


class Snake:
    head_colour = "white"
    body_colour = "green"

    def __init__(
        self, screen, base_segment_length, snake_width_factor, initial_segments
    ):
        from turtle import Turtle

        self.screen = screen

        self.base_snake_length = base_segment_length
        self.snake_width_factor = snake_width_factor
        self.snake_width = snake_width_factor * base_segment_length
        self.initial_length_factor = initial_segments

        # self.head_pos = [-self.snake_width / 2, 0]
        self.head_pos = [0, 0]

        def create_segment(index):
            return SnakeSegment(
                [self.head_pos[0] - index * self.snake_width, 0],
                self.base_snake_length,
                self.snake_width_factor,
                self.head_colour if index == 0 else self.body_colour,
            )

        self.body = [create_segment(index) for index in range(0, initial_segments)]

    # Move the snake forward one segment lenght.
    # The head just moves in whatever direction it is facing.
    # each segment must then move to the previous position of the segment ahead of it.
    def move(self):
        self.screen.tracer(False)

        for index, segment in enumerate(self.body):
            if 0 == index:
                segment.move_forward()
            else:
                # prev_segment_pos = self.body[index - 1].get_position()
                # prev_x = math.floor(prev_segment_pos[0])
                # prev_y = math.floor(prev_segment_pos[1])
                # segment_pos = segment.get_position()
                # seg_x = math.floor(segment_pos[0])
                # seg_y = math.floor(segment_pos[1])

                # if prev_x > seg_x:
                #     segment.face_right()
                # elif prev_x < seg_x:
                #     segment.face_left()
                # elif prev_y > seg_y:
                #     segment.face_up()
                # elif prev_y < seg_y:
                #     segment.face_down()

                # segment.move_forward()
                segment.move_to(self.body[index - 1].get_last_position())

        self.screen.update()
        time.sleep(0.1)

    def turn_left(self):
        self.body[0].turn_left()

    def turn_right(self):
        print("TURNING RIGHT")
        self.body[0].turn_right()
