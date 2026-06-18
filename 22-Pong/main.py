from turtle import Screen

from game import Game
from constants import GAME_WIDTH, GAME_HEIGHT


def prepare_screen():
    screen = Screen()

    screen.title("Pong")
    screen.bgcolor("black")
    screen.setup(width=GAME_WIDTH, height=GAME_HEIGHT)
    screen.tracer(0)
    return screen

def start_game():
    screen = prepare_screen()

    # The game is started by hitting the space bar.
    Game(screen)
    screen.exitonclick()

if __name__ == "__main__":
    start_game()