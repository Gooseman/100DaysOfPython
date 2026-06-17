from turtle import Screen

from game import Game
from constants import game_width, game_height


def prepare_screen():
    screen = Screen()

    screen.title("Pong")
    screen.bgcolor("black")
    screen.setup(width=game_width, height=game_height)
    screen.tracer(0)
    return screen

def start_game():
    screen = prepare_screen()

    # The game is started by hitting the space bar.
    Game(screen)
    screen.exitonclick()

if __name__ == "__main__":
    start_game()