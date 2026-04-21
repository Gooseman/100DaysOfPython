from random import randint, sample
from time import sleep

from car_lane import CarLane
from constants import base_square_size, game_height

from frog import Frog

class Game:
    def __init__(self, screen):
        self._game_running = False
        self._screen = screen#
        
        lane_width = 2 * base_square_size
        # Each lane is lane_width wide.  There are therefore game_height // lane_width lanes - 2. The first lane starts 
        # at lane_width and the last lane starts at game_height - lane_width
        number_of_lanes = game_height // lane_width - 2
        self._lanes = [CarLane(i) for i in range(0, number_of_lanes)]

        self.frog = Frog()
        self._prepare_key_bindings()
        self._screen.update()
        self._game_running = False
        self._collision = False
        self._reached_goal = False
    
    def reset_game(self):
        self.frog.reset()

        for lane in self._lanes:
            lane.reset()
        
        self._game_running = False
        self._collision = False
        self._reached_goal = False
        self._screen.update()
    
    def _prepare_key_bindings(self):
        self._screen.listen()
        self._screen.onkey(lambda: self._move_turtle(self.frog.move_up), "w")
        self._screen.onkey(lambda: self._move_turtle(self.frog.move_down), "s")
        self._screen.onkey(lambda: self._move_turtle(self.frog.move_left), "a")
        self._screen.onkey(lambda: self._move_turtle(self.frog.move_right), "d")
        self._screen.onkey(lambda: self._move_turtle(self.frog.move_left), "Left")
        self._screen.onkey(lambda: self._move_turtle(self.frog.move_right), "Right")
        self._screen.onkey(lambda: self._move_turtle(self.frog.move_up), "Up")
        self._screen.onkey(lambda: self._move_turtle(self.frog.move_down), "Down")
        self._screen.onkey(self.start_game, "space")

    def _move_turtle(self, move_function):
        if not self._game_running:
            print("Game is not running. Press space to start the game.")
            return
        
        move_function()
        self._screen.update()

    def start_game(self):
        if self._game_running:
            print("Game is already running.")
            return

        if self._collision:
            print("Collision detected. Resetting game.")
            self.reset_game()
            return
        
        if self._reached_goal:
            print("Congratulations! You've reached the goal!")
            self.reset_game()
            return
        
        print("Starting game...")
        self._game_running = True

        while self._game_running and not self._collision and not self._reached_goal:
            self._game_loop()
    
    def _game_loop(self):
        if self.has_reached_goal():
            print("Congratulations! You've reached the goal!")
            self._reached_goal = True
            self._game_running = False
            return
        
        self.move_cars()
        self.check_for_collisions()

        if self._collision:
            self._game_running = False
            return

        self.add_cars()
        sleep(0.25)
    
    def move_cars(self):
        for lane in self._lanes:
            lane.move_cars()
        
        self._screen.update()
    
    def has_reached_goal(self):
        return self.frog.get_y_position() >= (game_height / 2) - (2 * base_square_size)
    
    def check_for_collisions(self):
        # Determine which lane the frog is in based on its y coordinate.
        frog_position = self.frog.get_y_position()
        lane_number = int((frog_position + (game_height / 2)) // (2 * base_square_size) - 1)

        if lane_number < 0 or lane_number >= len(self._lanes):
            # The frog is not in a lane, so it cannot collide with a car
            return

        lane = self._lanes[lane_number]

        for car in lane._cars:
            if car.has_collided_with(self.frog.get_right_edge()):
                # self.reset_game()
                self._collision = True
                break
    
    def add_cars(self):
        # Get all lanes that can have a new car
        available_lanes = self._get_available_lanes()
        # Generate new cars in at most 2 of the available lanes
        new_car_lanes = sample(available_lanes, k=randint(0, min(2, len(available_lanes))))

        for lane in new_car_lanes:
            lane.add_car()

        self._screen.update()
    
    def _get_available_lanes(self):
        return [lane for lane in self._lanes if lane.is_available_for_new_car()]
