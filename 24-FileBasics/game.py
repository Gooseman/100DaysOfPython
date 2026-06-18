from time import sleep

class Game:
    def __init__(self, screen, food_placer, scoreboard, snake, turn_delay):
        self.screen = screen
        self.food_placer = food_placer
        self.scoreboard = scoreboard
        self.snake = snake
        self.turn_delay = turn_delay
        self._game_over = True

    def run_game(self):
        if not self._game_over:
            print("Game is already running.")
            return

        self._game_over = False
        current_turn_delay = self.turn_delay
        self._reset()

        self._place_food()

        while not self._game_over:
            current_turn_delay = self._play_game_turn(current_turn_delay)
            self._game_over = self.snake.has_collided()

            if self._game_over:
                self._on_game_over()
                current_turn_delay = self.turn_delay

    def _reset(self):
        self.scoreboard.reset()
        self.snake.reset()
        self.food_placer.clear_food()
        self.screen.update()

    def _place_food(self):
        self.food_placer.place_food(
            self.snake.get_snake_positions(),
            self.snake.get_snake_width(),
        )

    def _play_game_turn(self, turn_delay):
        print("Playing game turn")
        self.snake.move()
        self.screen.update()
        sleep(turn_delay)

        if self._has_eaten_food():
            self._handle_food_eaten()
            print(f"Turn delay before eating food: {turn_delay:.4f} seconds")
            return turn_delay * 0.98

        return turn_delay

    def _has_eaten_food(self):
        head_x, head_y = self.snake.get_snake_mouth_position()
        snake_width = self.snake.get_snake_width()
        head_x_range = [head_x - snake_width / 2, head_x + snake_width / 2]
        head_y_range = [head_y - snake_width / 2, head_y + snake_width / 2]
        food_x, food_y = self.food_placer.get_position()

        return (
            head_x_range[0] <= food_x <= head_x_range[1]
            and head_y_range[0] <= food_y <= head_y_range[1]
        )

    def _handle_food_eaten(self):
        self.snake.grow()
        self.food_placer.place_food(self.snake.get_snake_positions(), self.snake.get_snake_width())
        self.scoreboard.increase_score()

    def _on_game_over(self):
        self._handle_end_by_collision()

    def _handle_end_by_collision(self):
        print("Collision detected! Game over.")
        self.scoreboard.declare_game_over()
        self.screen.update()