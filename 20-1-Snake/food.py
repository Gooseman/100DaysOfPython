import math
import random
from turtle import Turtle


class Food:
    def __init__(self, food_size_factor, game_length, game_height):
        self.game_length, self.game_height = game_length, game_height

        self.base_size = 20
        self.food_size = self.base_size * food_size_factor

        self.food_placer = Turtle("circle")
        self.food_placer.penup()
        self.food_placer.color("red")
        self.food_placer.shapesize(stretch_len=food_size_factor, stretch_wid=food_size_factor)

    def place_food(self, snake_position: list, snake_width):
        self.food_placer.clear()

        food_pos = Food._get_food_position(
            snake_position, self.game_length, self.game_height, snake_width
        )

        self.food_placer.goto(food_pos[0], food_pos[1])
        self.food_placer.pendown()
        self.food_placer.dot(self.food_size)
        self.food_placer.penup()

    @staticmethod
    def _get_food_position(snake_position: list, game_length, game_height, snake_width):
        food_placed = False
        min_x = int(-math.floor(game_length / 2) + snake_width / 2)
        max_x = int(math.floor(game_length / 2) - snake_width / 2)
        min_y = int(-math.floor(game_height / 2) + snake_width / 2)
        max_y = int(math.floor(game_height / 2) - snake_width / 2)

        while not food_placed:
            food_pos = [
                Food._coord_to_nearest_grid(random.randint(min_x, max_x), snake_width),
                Food._coord_to_nearest_grid(random.randint(min_y, max_y), snake_width),
            ]

            if (food_pos[0], food_pos[1]) not in snake_position:
                print("FOOD POSITION:", food_pos)
                return food_pos
        
        raise Exception("Unable to place food on the board without colliding with the snake.")

    @staticmethod
    def _coord_to_nearest_grid(coordinate, grid_size):
        return math.floor(round(coordinate / grid_size) * grid_size)

    def get_position(self):
        return self.food_placer.position()
