from turtle import Screen

from game import Game
from ball import Ball
from constants import game_width, game_height
from court import Court
from paddle import Paddle
from scoreboard import Scoreboard


def prepare_screen():
    screen = Screen()

    screen.title("Pong")
    screen.bgcolor("black")
    screen.setup(width=game_width, height=game_height)
    screen.tracer(0)
    return screen


def start_game():

    pass


if __name__ == "__main__":
    screen = prepare_screen()

    game = Game(screen)

    # game.start_game()
    screen.exitonclick()
