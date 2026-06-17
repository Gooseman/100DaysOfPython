import math
from turtle import Turtle

class SnakeSegment:
    def __init__(self, position, base_size, size_factor, colour="white"):
        self.size = base_size * size_factor
        self.segment = Turtle("square")

        self.segment.color(colour)
        self.segment.speed("fastest")
        self.segment.penup()
        self.segment.goto(position)
        self.last_position = position
        self.segment.resizemode("user")
        self.segment.shapesize(stretch_len=size_factor, stretch_wid=size_factor)

    def move_forward(self):
        # print("moving from position:", self.segment.position())
        self.last_position = [math.floor(coord) for coord in self.segment.position()]
        self.segment.forward(self.size)
        # print("moved to position:", self.segment.position())

    def move_to(self, position):
        new_position = [math.floor(coord) for coord in position]

        self.last_position = self.segment.position()
        self.segment.goto(new_position)

    def turn_left(self):
        self.segment.left(90)

    def turn_right(self):
        self.segment.right(90)

    def face_left(self):
        self.segment.setheading(180)

    def face_right(self):
        self.segment.setheading(0)

    def face_up(self):
        self.segment.setheading(90)

    def face_down(self):
        self.segment.setheading(270)

    def get_position(self):
        return self.segment.position()

    def get_last_position(self):
        return self.last_position

    def will_collide(
        self, game_left, game_right, game_top, game_bottom, body_positions
    ):
        x, y = [math.floor(coord) for coord in self.get_position()]
        heading = self.segment.heading()

        match heading:
            case 0:
                return self._will_collide_to_the_right(x, y, game_right, body_positions)

            case 90:
                return self._will_collide_upwards(x, y, game_top, body_positions)

            case 180:
                return self._will_collide_to_the_left(x, y, game_left, body_positions)

            case 270:
                return self._will_collide_downwards(x, y, game_bottom, body_positions)

            case _:
                return False

    def _will_collide_to_the_right(self, x, y, game_right, body_positions):
        new_x = x + self.size

        return new_x > game_right or (new_x, y) in body_positions

    def _will_collide_to_the_left(self, x, y, game_left, body_positions):
        new_x = x - self.size

        return new_x < game_left or (new_x, y) in body_positions

    def _will_collide_upwards(self, x, y, game_top, body_positions):
        new_y = y + self.size

        return new_y > game_top or (x, new_y) in body_positions

    def _will_collide_downwards(self, x, y, game_bottom, body_positions):
        new_y = y - self.size

        return new_y < game_bottom or (x, new_y) in body_positions
