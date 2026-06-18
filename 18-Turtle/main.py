import random
from turtle import Turtle, Screen

import colorgram

DOT_SIZE = 10

def dashed_line(the_turtle, length, dash_length):
    for _ in range(length // dash_length):
        the_turtle.pendown()
        the_turtle.forward(dash_length)
        the_turtle.penup()
        the_turtle.forward(dash_length)

def draw_shape(the_turtle, side_length, sides):
    angle = 360 / sides

    for _ in range(sides):
        the_turtle.forward(side_length)
        the_turtle.right(angle)

def random_colour():
    red = random.random()
    green = random.random()
    blue = random.random()

    return (red, green, blue)

def draw_all_shapes(the_turtle, side_length):
    for sides in range(3, 11):
        the_turtle.color(random_colour())
        draw_shape(the_turtle, side_length, sides)

def random_walk(the_turtle, steps, step_length):
    directions = [0, 90, 180, 270]

    the_turtle.width(5)
    the_turtle.speed('fastest')

    for _ in range(steps):
        the_turtle.color(random_colour())
        the_turtle.setheading(random.choice(directions))
        the_turtle.forward(step_length)

def spirograph(the_turtle, radius, angle):
    the_turtle.speed('fastest')
    the_turtle.width(2)

    for _ in range(int(360 / angle)):
        the_turtle.color(random_colour())
        the_turtle.circle(radius)
        the_turtle.setheading(the_turtle.heading() + angle)

def spirograph01(the_turtle, min_radius, max_radius, angle):
    the_turtle.speed('fastest')
    the_turtle.width(2)

    current_circle = 0

    for _ in range(int(360 // angle)):
        the_turtle.color(random_colour())

        if (current_circle % 2) == 0:
            radius = min_radius
        else:
            radius = max_radius

        current_circle += 1
        the_turtle.circle(radius)
        the_turtle.setheading(the_turtle.heading() + angle)

def get_colours():
    colours = colorgram.extract(r'D:\MMedia\Images\spires_by_itsthemojo_d2y4aa3.jpg', 8)

    def get_colour_tuple(colour):
        r = colour.rgb.r
        g = colour.rgb.g
        b = colour.rgb.b

        return (r, g, b)

    return [get_colour_tuple(colour) for colour in colours]

def get_random_colours(num_colours):
    def get_colour_tuple():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        return (r, g, b)

    return [get_colour_tuple() for _ in range(num_colours)]

def draw_dot_grid(the_turtle, num_rows, num_cols, dot_size, spacing):
    colours = get_random_colours(10)

    the_turtle.hideturtle()
    the_turtle.speed('fastest')
    the_turtle.penup()
    the_turtle.goto(-spacing * num_cols / 2, -spacing * num_rows / 2)

    for _ in range(num_rows):
        for _ in range(num_cols):
            the_turtle.pendown()
            the_turtle.dot(dot_size, random.choice(colours))
            the_turtle.penup()
            the_turtle.forward(spacing)

        the_turtle.penup()
        the_turtle.left(90)
        the_turtle.forward(spacing)
        the_turtle.left(90)
        the_turtle.forward(spacing * num_cols)
        the_turtle.left(180)

def do_run():
    screen = Screen()
    the_turtle = Turtle()

    # the_turtle.shape("the_turtle")
    # the_turtle.color("blue")

    # draw_all_shapes(the_turtle, 50)
    # random_walk(the_turtle, 20, 20)
    # spirograph(the_turtle, 100, 5)
    # spirograph01(the_turtle, 100, 150, 10)
    screen.colormode(255)
    draw_dot_grid(the_turtle, 10, 10, 25, 15)

    the_turtle.color('')
    # Keep this at the bottom to exit
    screen.exitonclick()

if __name__ == '__main__':
    do_run()
