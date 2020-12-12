import re
import sys
from dataclasses import dataclass
import math

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day12/"

# Part 1

# Class here with be ship
#


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


@dataclass
class Instruction:
    action: str
    value: int


def parse_input(input):
    instructions = []
    for line in input:
        action = line[0]
        value = int(line[1:])
        instruction = Instruction(action, value)
        instructions.append(instruction)

    return instructions


class Ship:
    def __init__(self, x_pos=0, y_pos=0, direction=90):
        # X is the east, west. With east +ve, and west -ve
        self.x_pos = x_pos

        # Y is the north, south. With north +ve, and south -ve
        self.y_pos = y_pos

        # Degress from north, i.e. the line x=0
        self.direction = direction

    def do_instruction(self, action, value):
        if action == "N":
            self.y_pos += value
        elif action == "S":
            self.y_pos -= value
        elif action == "E":
            self.x_pos += value
        elif action == "W":
            self.x_pos -= value
        elif action == "L":
            self.update_direction(-value)
        elif action == "R":
            self.update_direction(+value)
        elif action == "F":
            self.move_forward(value)

    # We want direction always to be a value between
    # 0 and 360
    def update_direction(self, value):
        self.direction += value
        if self.direction > 360:
            self.direction -= 360
        elif self.direction < 0:
            self.direction += 360

    def move_forward(self, value):
        # Assume degrees are multiple of 90, therefore
        # can just round the result of sin and cos
        self.x_pos += value * round(math.sin(math.radians(self.direction)))
        self.y_pos += value * round(math.cos(math.radians(self.direction)))

    def get_distance(self, x, y):
        return abs(self.x_pos - x) + abs(self.y_pos - y)


def part1_solve(instructions):
    # Start east, so direction 90
    ship = Ship(x_pos=0, y_pos=0, direction=90)
    for instruction in instructions:
        ship.do_instruction(instruction.action, instruction.value)

    return ship.get_distance(0, 0)


if __name__ == "__main__":

    test_input = parse_input(get_input(PATH + "test_input"))
    print(part1_solve(test_input))

    real_input = parse_input(get_input(PATH + "real_input"))
    print(part1_solve(real_input))
