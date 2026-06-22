from turtle import Screen

from frogger.constants import GAME_WIDTH, GAME_HEIGHT
from frogger.game import Game

def prepare_screen():
    screen = Screen()

    screen.title("Frogger")
    screen.bgcolor("black")
    screen.setup(width=GAME_WIDTH, height=GAME_HEIGHT)
    screen.tracer(0)
    return screen

def run_game():
    screen = prepare_screen()

    Game(screen) # pylint: disable=no-value-for-parameter
    screen.exitonclick()

if __name__ == "__main__":
    run_game()
