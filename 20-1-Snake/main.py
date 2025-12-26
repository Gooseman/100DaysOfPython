from turtle import Turtle, Screen
from snake import Snake

if __name__ == "__main__":
    base_snake_length = 20
    snake_width_factor = 0.5
    snake_initial_segments = 6
    snake_initial_length_factor = snake_initial_segments * snake_width_factor
    screen = Screen()
    screen.title("Snake")
    screen.setup(width=600, height=600)
    screen.bgcolor("black")

    snake = Snake(screen, base_snake_length, snake_width_factor, snake_initial_segments)

    snake.turn_left()
    snake.move()
    snake.move()
    snake.move()
    snake.turn_right()
    snake.move()
    snake.move()
    snake.move()
    snake.turn_right()
    snake.move()
    snake.move()
    snake.move()
    snake.move()
    snake.move()

    screen.exitonclick()
