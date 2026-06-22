import random


class TurtleRace:
    def __init__(self, turtles, race_end, bet):
        self.turtles = turtles
        self.race_length = race_end
        self.bet = bet

    def race(self):
        while all(racer.get_position() < self.race_length for racer in self.turtles):
            for turtle in self.turtles:
                turtle.move_forward(random.randint(1, 10))

        self.declare_winner()

    def declare_winner(self):
        winner = max(self.turtles, key=lambda t: t.get_position()).name

        print(f"The winner is {winner}!")

        if winner == self.bet:
            print("Congratulations! You won your bet!")
        else:
            print("Sorry, you lost your bet.")
