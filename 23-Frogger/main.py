from turtle import Screen

from constants import game_width, game_height
from game import Game

def prepare_screen():
    screen = Screen()

    screen.title("Frogger")
    screen.bgcolor("black")
    screen.setup(width=game_width, height=game_height)
    screen.tracer(0)
    return screen

if __name__ == "__main__":
    screen = prepare_screen()
    game = Game(screen)

    screen.exitonclick()
