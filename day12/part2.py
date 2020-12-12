import re
import sys
from dataclasses import dataclass
import math
import numpy

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


@dataclass
class Waypoint:
    x_pos: int
    y_pos: int

    def rotate(self, value):
        # Convert to polar coordinates
        # Do degrees from north to be consistent
        # x = r * sin(angle)
        # y = r * cos(angle)
        radius = math.sqrt((self.x_pos ** 2) + (self.y_pos ** 2))
        angle = math.degrees(numpy.arctan2(self.x_pos, self.y_pos))

        # Add degrees
        angle += value

        if angle > 360:
            angle -= 360
        elif angle < 0:
            angle += 360

        # Re-calcutate x and y by converting to cartesian
        # also round here, as assume angles will be nice...
        self.x_pos = round(radius * math.sin(math.radians(angle)))
        self.y_pos = round(radius * math.cos(math.radians(angle)))


class Ship:
    def __init__(
        self,
        wp_x_pos,
        wp_y_pos,
        x_pos=0,
        y_pos=0,
        direction=90,
    ):
        # X is the east, west. With east +ve, and west -ve
        self.x_pos = x_pos

        # Y is the north, south. With north +ve, and south -ve
        self.y_pos = y_pos

        self.waypoint = Waypoint(wp_x_pos, wp_y_pos)

    def do_instruction(self, action, value):
        # Move waypoint north, south, east or west
        if action == "N":
            self.waypoint.y_pos += value
        elif action == "S":
            self.waypoint.y_pos -= value
        elif action == "E":
            self.waypoint.x_pos += value
        elif action == "W":
            self.waypoint.x_pos -= value

        # Rotate the waypoint around the ship
        elif action == "L":
            self.waypoint.rotate(-value)
        elif action == "R":
            self.waypoint.rotate(+value)

        # Move ship a number of times in direction of waypoint
        elif action == "F":
            self.move_ship(value)

    def move_ship(self, value):
        # Move the ship relative to weighpoint
        self.x_pos += value * self.waypoint.x_pos
        self.y_pos += value * self.waypoint.y_pos

    def get_distance(self, x, y):
        return abs(self.x_pos - x) + abs(self.y_pos - y)


def part2_solve(instructions):
    # Start east, so direction 90
    ship = Ship(x_pos=0, y_pos=0, direction=90, wp_x_pos=10, wp_y_pos=1)

    for instruction in instructions:
        ship.do_instruction(instruction.action, instruction.value)

    return ship.get_distance(0, 0)


if __name__ == "__main__":

    test_input = parse_input(get_input(PATH + "test_input"))
    print(part2_solve(test_input))

    test_input = parse_input(get_input(PATH + "test_input_1"))
    print(part2_solve(test_input))

    real_input = parse_input(get_input(PATH + "real_input"))
    print(part2_solve(real_input))
