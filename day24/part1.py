import re
import sys
from dataclasses import dataclass
import math
import copy

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day24/"

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def parse_input(input):
    output = []
    for directions_str in input:
        directions = []
        while directions_str != "":
            if (
                directions_str.startswith("se")
                or directions_str.startswith("sw")
                or directions_str.startswith("ne")
                or directions_str.startswith("nw")
            ):
                directions.append(directions_str[:2])
                directions_str = directions_str[2:]
            elif directions_str.startswith("w") or directions_str.startswith("e"):
                directions.append(directions_str[:1])
                directions_str = directions_str[1:]

        output.append(directions)
    return output


# Every point on a hexagonal gird (and indeed any 2D space) can be reached
# by a combinations of 2 non-parallel vectors
# Choose 2 vectors here, and the coordinates will be the scalar infront
# to get to the grid
# Vectors we choose will be "e", and "ne"
def convert_dirs_to_coords(directions):
    # Directions are relative to a base coord, call that 0,0
    coords = [0, 0]

    for direction in directions:
        if direction == "e":
            coords[0] += 1
        elif direction == "w":
            coords[0] -= 1
        elif direction == "ne":
            coords[1] += 1
        elif direction == "sw":
            coords[1] -= 1
        elif direction == "se":
            coords[0] += 1
            coords[1] -= 1
        elif direction == "nw":
            coords[0] -= 1
            coords[1] += 1
    return coords


def part1_solve(dir_list):
    black_squares = []

    for directions in dir_list:
        coord = convert_dirs_to_coords(directions)

        if coord not in black_squares:
            black_squares.append(coord)
        else:
            black_squares.remove(coord)

    return len(black_squares)


if __name__ == "__main__":
    input = parse_input(get_input(PATH + "test_input"))
    print(part1_solve(input))

    input = parse_input(get_input(PATH + "real_input"))
    print(part1_solve(input))
