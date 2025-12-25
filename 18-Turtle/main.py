import random
from turtle import Turtle, Screen, colormode

import colorgram

dot_size = 10

def dashed_line(turtle, length, dash_length):
    for _ in range(length // dash_length):
        turtle.pendown()
        turtle.forward(dash_length)
        turtle.penup()
        turtle.forward(dash_length)

def draw_shape(turtle, side_length, sides):
    angle = 360 / sides

    for _ in range(sides):
        turtle.forward(side_length)
        turtle.right(angle)

def random_colour():
    red = random.random()
    green = random.random()
    blue = random.random()

    return (red, green, blue)
                         
def draw_all_shapes(turtle, side_length):
    for sides in range(3, 11):
        turtle.color(random_colour())
        draw_shape(turtle, side_length, sides)

def random_walk(turtle, steps, step_length):
    directions = [0, 90, 180, 270]
    
    turtle.width(5)
    turtle.speed('fastest')

    for _ in range(steps):
        turtle.color(random_colour())
        turtle.setheading(random.choice(directions))
        turtle.forward(step_length)

def spirograph(turtle, radius, angle):
    turtle.speed('fastest')
    turtle.width(2)

    for _ in range(int(360 / angle)):
        turtle.color(random_colour())
        turtle.circle(radius)
        turtle.setheading(turtle.heading() + angle)

def spirograph01(turtle, min_radius, max_radius, angle):
    turtle.speed('fastest')
    turtle.width(2)

    current_circle = 0

    for _ in range(int(360 // angle)):
        turtle.color(random_colour())

        if (current_circle % 2) == 0:
            radius = min_radius
        else:
            radius = max_radius

        current_circle += 1
        turtle.circle(radius)
        turtle.setheading(turtle.heading() + angle)

def get_colours():
    colours = colorgram.extract('D:\MMedia\Images\spires_by_itsthemojo_d2y4aa3.jpg', 8)

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

def draw_dot_grid(turtle, num_rows, num_cols, dot_size, spacing):
    colours = get_random_colours(10)

    turtle.hideturtle()
    turtle.speed('fastest')
    colormode(255)
    turtle.penup()
    turtle.goto(-spacing * num_cols / 2, -spacing * num_rows / 2)

    for _ in range(num_rows):
        for _ in range(num_cols):
            turtle.pendown()
            turtle.dot(dot_size, random.choice(colours))
            turtle.penup()
            turtle.forward(spacing)
        
        turtle.penup()
        turtle.left(90)
        turtle.forward(spacing)
        turtle.left(90)
        turtle.forward(spacing * num_cols)
        turtle.left(180)

if __name__ == '__main__':
    screen = Screen()
    turtle = Turtle()

    # turtle.shape("turtle")
    # turtle.color("blue")

    # draw_all_shapes(turtle, 50)
    # random_walk(turtle, 20, 20)
    # spirograph(turtle, 100, 5)
    # spirograph01(turtle, 100, 150, 10)
    draw_dot_grid(turtle, 10, 10, 25, 15)

    turtle.color('')
    # Keep this at the bottom to exit
    screen.exitonclick()