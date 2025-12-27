import math
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake


def run_game():
    food_placer = Food(screen, 0.4)
    scoreboard = Scoreboard(game_height)

    food_placer.place_food(
        snake.get_snake_positions(),
        snake.get_snake_width(),
    )

    while not snake.has_collided():
        play_game_turn(snake, food_placer, scoreboard)

    if snake.has_collided():
        handle_end_by_collision(scoreboard)
    else:
        print("No collision detected in 10 moves.")


def play_game_turn(snake, food_placer, scoreboard):
    snake.move()

    if has_eaten_food(snake, food_placer):
        handle_food_eaten(snake, food_placer, scoreboard)

def has_eaten_food(snake, food_placer):
    head_x, head_y = snake.get_snake_mouth_position()
    snake_width = snake.get_snake_width()
    head_x_range = [head_x - snake_width / 2, head_x + snake_width / 2]
    head_y_range = [head_y - snake_width / 2, head_y + snake_width / 2]
    food_x, food_y = food_placer.get_position()

    return (
        head_x_range[0] <= food_x
        and food_x <= head_x_range[1]
        and head_y_range[0] <= food_y
        and food_y <= head_y_range[1]
    )


def handle_food_eaten(snake, food_placer, scoreboard):
    snake.grow()
    food_placer.place_food(snake.get_snake_positions(), snake.get_snake_width())
    scoreboard.increase_score()


def handle_end_by_collision(scoreboard):
    print("Collision detected! Game over.")
    scoreboard.declare_game_over()


# Main program
if __name__ == "__main__":
    base_snake_length = 20
    snake_width_factor = 0.75
    snake_initial_segments = 8
    snake_initial_length_factor = snake_initial_segments * snake_width_factor
    game_length = 600
    game_height = 600
    screen = Screen()
    screen.title("Snake")
    screen.setup(width=game_length, height=game_height)
    screen.bgcolor("black")
    screen.tracer(False)

    snake = Snake(
        screen,
        base_snake_length,
        snake_width_factor,
        snake_initial_segments,
        game_length,
        game_height,
    )

    screen.onkey(snake.turn_left, "Left")
    screen.onkey(snake.turn_right, "Right")
    screen.listen()

    run_game()

    screen.exitonclick()
