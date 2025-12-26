from turtle import Turtle, Screen
from RacingTurtle import RacingTurtle
from TurtleRace import TurtleRace


def etch_a_sketch(screen):
    def move_forwards():
        turtle.forward(10)

    def move_backwards():
        turtle.backward(10)

    def on_left_press():
        turtle.left(10)

    def on_right_press():
        turtle.right(10)

    def turn_up():
        turtle.setheading(90)

    def turn_down():
        turtle.setheading(270)

    def turn_right():
        turtle.setheading(0)

    def turn_left():
        turtle.setheading(180)

    def reset_drawing():
        turtle.clear()
        turtle.penup()
        turtle.home()
        turtle.pendown()

    turtle = Turtle()

    turtle.speed("fastest")
    screen.listen()

    screen.onkeypress(move_forwards, "Up")
    screen.onkeypress(on_left_press, "Left")
    screen.onkeypress(move_backwards, "Down")
    screen.onkeypress(on_right_press, "Right")
    screen.onkey(turn_up, "w")
    screen.onkey(turn_down, "s")
    screen.onkey(turn_right, "d")
    screen.onkey(turn_left, "a")
    screen.onkey(reset_drawing, "c")


def turtle_race(screen):
    screen.setup(width=500, height=400)
    turtle_names = [
        "Tim",
        "Jan",
        "Tom",
        "Sue",
        "Seth",
    ]

    bet = take_bet(screen, turtle_names)

    turtles = [
        RacingTurtle(turtle_names[0], "red"),
        RacingTurtle(turtle_names[1], "blue"),
        RacingTurtle(turtle_names[2], "green"),
        RacingTurtle(turtle_names[3], "orange"),
        RacingTurtle(turtle_names[4], "purple"),
    ]

    for index, t in enumerate(turtles):
        t.turtle.speed("fastest")
        t.set_postion(-230, -100 + (index * 50))

    race = TurtleRace(turtles, 230, bet)

    race.race()


def take_bet(self, turtle_names):
    return screen.textinput(
        "Make your bet", f"Which turtle will win the race? {turtle_names}: "
    )


if __name__ == "__main__":
    screen = Screen()

    # etch_a_sketch(screen)
    turtle_race(screen)

    screen.exitonclick()
