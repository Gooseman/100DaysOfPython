from random import choice

from car import Car
from constants import BASE_SQUARE_SIZE, CAR_SPEEDS, GAME_HEIGHT, GAME_WIDTH

class CarLane:
    def __init__(self, lane_number):
        self._lane_number = lane_number
        self._cars = []
        self._speed = choice(CAR_SPEEDS)

    def get_speed(self):
        return self._speed

    def increase_speed(self):
        self._speed += BASE_SQUARE_SIZE * 0.5

    def is_available_for_new_car(self):
        # A lane can have a car added if the right end of the last car in the lane is at least 2 base_square_siz
        # away from the edge of the screen
        return (len(self._cars) == 0) \
            or (self._cars[-1].get_right_edge() < (GAME_WIDTH / 2) - (6 * BASE_SQUARE_SIZE))

    def add_car(self):
        y_position = (self._lane_number + 1) * 2 * BASE_SQUARE_SIZE + BASE_SQUARE_SIZE - GAME_HEIGHT / 2
        new_car = Car((GAME_WIDTH / 2, y_position), speed=self._speed)

        self._cars.append(new_car)

    def move_cars(self):
        for car in self._cars:
            car.move()

    def reset(self):
        print(f"Resetting lane {self._lane_number} with {len(self._cars)} cars.")
        for car in self._cars:
            car.clear()
            car.hideturtle()
            car.reset()

        self._cars = []
    
    def cars(self):
        return self._cars
