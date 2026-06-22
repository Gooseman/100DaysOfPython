from turtle import Turtle, Screen

from etch_a_sketch.racing_turtle import RacingTurtle
from etch_a_sketch.turtle_race import TurtleRace


def etch_a_sketch(screen):
    def move_forwards():
        the_turtle.forward(10)

    def move_backwards():
        the_turtle.backward(10)

    def on_left_press():
        the_turtle.left(10)

    def on_right_press():
        the_turtle.right(10)

    def turn_up():
        the_turtle.setheading(90)

    def turn_down():
        the_turtle.setheading(270)

    def turn_right():
        the_turtle.setheading(0)

    def turn_left():
        the_turtle.setheading(180)

    def reset_drawing():
        the_turtle.clear()
        the_turtle.penup()
        the_turtle.home()
        the_turtle.pendown()

    the_turtle = Turtle()

    the_turtle.speed("fastest")
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

    for index, the_turtle in enumerate(turtles):
        the_turtle.turtle.speed("fastest")
        the_turtle.set_postion(-230, -100 + (index * 50))

    race = TurtleRace(turtles, 230, bet)

    race.race()


def take_bet(screen, turtle_names):
    return screen.textinput(
        "Make your bet", f"Which turtle will win the race? {turtle_names}: "
    )

def do_run():
    screen = Screen()

    # etch_a_sketch(screen)
    turtle_race(screen)

    screen.exitonclick()

if __name__ == "__main__":
    do_run()
