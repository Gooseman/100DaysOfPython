import math
import random

from turtle import Screen, Turtle
from snake import Snake


def create_food_turtle():
    food_turtle = Turtle()
    food_turtle.hideturtle()
    food_turtle.penup()

    return food_turtle


def add_food(food_placer, snake_position, game_length, game_height, snake_width):
    food_pos = get_food_position(snake_position, game_length, game_height, snake_width)

    food_placer.pencolor("red")
    food_placer.shapesize(stretch_wid=0.5, stretch_len=0.5)
    food_placer.goto(food_pos[0], food_pos[1])
    food_placer.pendown()
    food_placer.dot(snake_width)
    food_placer.penup()


def get_food_position(snake_position, game_length, game_height, snake_width):
    food_placed = False
    min_x = int(-math.floor(game_length / 2) + snake_width)
    print("MIN X:", min_x)
    max_x = int(math.floor(game_length / 2) - snake_width)
    print("MAX X:", max_x)
    min_y = int(-math.floor(game_height / 2) + snake_width)
    print("MIN Y:", min_y)
    max_y = int(math.floor(game_height / 2) - snake_width)
    print("MAX Y:", max_y)

    while not food_placed:
        food_pos = [random.randint(min_x, max_x), random.randint(min_y, max_y)]

        if (food_pos[0], food_pos[1]) not in snake_position:
            return food_pos


if __name__ == "__main__":
    base_snake_length = 20
    snake_width_factor = 0.5
    snake_initial_segments = 8
    snake_initial_length_factor = snake_initial_segments * snake_width_factor
    game_length = 600
    game_height = 600
    screen = Screen()
    screen.title("Snake")
    screen.setup(width=game_length, height=game_height)
    screen.bgcolor("black")

    snake = Snake(
        screen,
        base_snake_length,
        snake_width_factor,
        snake_initial_segments,
        game_length,
        game_height,
    )
    food_placer = create_food_turtle()
    food = add_food(
        food_placer,
        snake.get_snake_positions(),
        game_length,
        game_height,
        snake.get_snake_width(),
    )

    screen.onkey(snake.turn_left, "Left")
    screen.onkey(snake.turn_right, "Right")
    screen.listen()

    move_count = 0

    while not snake.has_collided():
        snake.move()
        move_count += 1

        if move_count > 10:
            snake.grow()
            move_count = 0

    if snake.has_collided():
        print("Collision detected! Game over.")

    else:
        print("No collision detected in 10 moves.")

    screen.exitonclick()
