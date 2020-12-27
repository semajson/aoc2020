import re
import sys
from dataclasses import dataclass
import math
import copy
import numpy as np

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
    return tuple(coords)


class Tiles:
    def __init__(self, black_tiles):
        self.black_tiles = black_tiles

    def get_surr_tiles(self, coords):
        coords = list(coords)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [-1, 1]]

        surr = []
        for dir in directions:
            surr.append(np.add(coords, dir))

        return [tuple(i) for i in surr]

    def count_surr_black(self, coords):
        surr_tiles = self.get_surr_tiles(coords)
        count = 0
        for surr_tile in surr_tiles:
            if surr_tile in self.black_tiles:
                count += 1
        return count

    # Maybe we could keep a cache of all the tiles we need to update?
    def white_tiles_to_update(self):
        # Loop through all the black tiles,
        # any white tiles surrounding them need updating
        white_tiles = set()
        for black_tile in self.black_tiles:
            surr_tiles = self.get_surr_tiles(black_tile)
            for surr_tile in surr_tiles:
                if surr_tile not in self.black_tiles:
                    white_tiles.add(surr_tile)

        return white_tiles

    def run_day(self):
        new_black_tiles = []

        for black_tile in self.black_tiles:
            surr_black = self.count_surr_black(black_tile)
            if (surr_black == 1) or (surr_black == 2):
                new_black_tiles.append(black_tile)

        for white_tile in self.white_tiles_to_update():
            surr_black = self.count_surr_black(white_tile)
            if surr_black == 2:
                new_black_tiles.append(white_tile)

        self.black_tiles = new_black_tiles

    def run_days(self, days):
        for _ in range(days):
            self.run_day()
            print(_)

    def get_black_tiles(self):
        return len(self.black_tiles)


def part2_solve(dir_list):
    black_tiles = set()

    for directions in dir_list:
        coord = convert_dirs_to_coords(directions)

        if coord not in black_tiles:
            black_tiles.add(coord)
        else:
            black_tiles.remove(coord)

    tiles = Tiles(black_tiles)
    tiles.run_days(100)

    return tiles.get_black_tiles()


if __name__ == "__main__":
    input = parse_input(get_input(PATH + "test_input"))
    print(part2_solve(input))

    input = parse_input(get_input(PATH + "real_input"))
    print(part2_solve(input))
