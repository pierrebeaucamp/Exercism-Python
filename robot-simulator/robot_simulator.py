import itertools

NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)

class Robot:
    def __init__(self, b=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.__directions = itertools.cycle([NORTH, EAST, SOUTH, WEST])
        self.turn_right()
        while self.bearing != b: self.turn_right()

    def advance(self):
        self.coordinates = tuple(map(sum,zip(self.coordinates, self.bearing)))

    def simulate(self, command):
        for c in command:
            if c == "L": self.turn_left()
            if c == "R": self.turn_right()
            if c == "A": self.advance()

    def turn_left(self):
        for _ in range(3): self.turn_right()

    def turn_right(self):
        self.bearing = next(self.__directions)
