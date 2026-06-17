from turtle import Screen

from food import Food
from game import Game
from scoreboard import Scoreboard
from snake import Snake

def run_game():
    base_snake_length = 20
    snake_width_factor = 0.75
    snake_initial_segments = 8
    game_length = 600
    game_height = 600
    screen = Screen()
    screen.title("Snake")
    screen.setup(width=game_length, height=game_height)
    screen.bgcolor("black")
    screen.tracer(False)

    snake = Snake(base_snake_length, snake_width_factor, snake_initial_segments, game_length, game_height)
    food_placer = Food(0.4, game_length, game_height)
    scoreboard = Scoreboard(game_height)
    turn_delay = 0.1
    game = Game(screen, food_placer, scoreboard, snake, turn_delay)

    screen.onkey(snake.turn_left, "Left")
    screen.onkey(snake.turn_right, "Right")
    screen.onkey(game.run_game, "space")
    screen.listen()

    # game.run_game()
    screen.exitonclick()

if __name__ == "__main__":
    run_game()
