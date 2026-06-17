from turtle import Screen

from constants import GAME_WIDTH, GAME_HEIGHT
from game import Game

def prepare_screen():
    screen = Screen()

    screen.title("Frogger")
    screen.bgcolor("black")
    screen.setup(width=GAME_WIDTH, height=GAME_HEIGHT)
    screen.tracer(0)
    return screen

def run_game():
    screen = prepare_screen()

    Game(screen)
    screen.exitonclick()

if __name__ == "__main__":
    run_game()