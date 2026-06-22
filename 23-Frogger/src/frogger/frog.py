from turtle import Turtle

from frogger.constants import BASE_SQUARE_SIZE, GAME_WIDTH, GAME_HEIGHT

class Frog(Turtle):
    _move_size = BASE_SQUARE_SIZE * 2

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.reset()

    def reset(self):
        print("Resetting frog position.")
        self.goto(0, -GAME_HEIGHT / 2 + BASE_SQUARE_SIZE)
        self.setheading(90)

    def move_up(self):
        if (self.ycor() + self._move_size) >= (GAME_HEIGHT / 2):
            return

        self.setheading(90)
        self.forward(self._move_size)

    def move_down(self):
        if (self.ycor() - self._move_size) <= -(GAME_HEIGHT / 2):
            return

        self.setheading(90)
        self.backward(self._move_size)

    def move_left(self):
        if (self.xcor() - self._move_size) <= -(GAME_WIDTH / 2):
            return

        self.setheading(180)
        self.forward(self._move_size)

    def move_right(self):
        if (self.xcor() + self._move_size) >= (GAME_WIDTH / 2):
            return

        self.setheading(0)
        self.forward(self._move_size)

    def get_right_edge(self):
        return self.xcor() + BASE_SQUARE_SIZE / 2

    def get_y_position(self):
        return self.ycor()
