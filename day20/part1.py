import re
import sys
from dataclasses import dataclass
import math
import copy

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day20/"

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


class Tile:
    def __init__(self, name, tile):
        self.name = name
        self.tile = tile

    def __repr__(self):
        return str(self.tile)

    def __str__(self):
        return str(self.tile)

    def get_edges(self):
        edges = []

        # top and bottom edges
        edges.append(self.tile[0].copy())
        edges.append(self.tile[len(self.tile) - 1].copy())

        # left and right edges
        edges.append([line[0] for line in self.tile])
        edges.append([line[len(self.tile) - 1] for line in self.tile])

        return edges

    def does_edge_match_tile(self, input_edge):
        match_edge = False

        # Do the rotations
        for edge in self.get_edges():
            if input_edge == edge:
                assert not match_edge
                match_edge = True
                # print("Edge in", edge)
                # print("edge match", input_edge)

        # Do reflection and then rotations
        for edge in self.get_edges():
            edge.reverse()
            if input_edge == edge:
                assert not match_edge
                match_edge = True

        return match_edge


class Image:
    def __init__(self, tiles):
        self.tiles = []
        current_name = None
        current_tile = []

        for line in tiles:
            if line.startswith("Tile"):
                # Save current tiles
                if current_name != None:
                    self.tiles.append(Tile(current_name, current_tile))
                    current_tile = []
                current_name = line.replace("Tile ", "").replace(":", "")
            elif line != "":
                current_tile.append(list(line))

        # Add the last image
        self.tiles.append(Tile(current_name, current_tile))

    def get_corners(self):
        corners = []
        for tile in self.tiles:
            num_neigh = 0

            for edge in tile.get_edges():
                for neigh_tile in self.tiles:
                    if tile == neigh_tile:
                        continue
                    if neigh_tile.does_edge_match_tile(edge):
                        num_neigh += 1

            if num_neigh == 2:
                corners.append(tile)
        return corners

    def arrange_tiles(self):
        # Start with the top corner
        corners = self.get_corners()
        top_corner = corners[0]


def part1_solve(input):
    image = Image(input)

    corners = image.get_corners()

    product = 1
    for corner in corners:
        product *= int(corner.name)
    return product


def part2_solve(input):
    image = Image(input)

    # Start with the top corner
    image.arrange_tiles()


if __name__ == "__main__":
    input = get_input(PATH + "test_input")
    print(part1_solve(input))

    # input = get_input(PATH + "real_input")
    # print(part1_solve(input))
