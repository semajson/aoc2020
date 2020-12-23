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

    def get_right_edge(self):
        return [line[len(self.tile) - 1] for line in self.tile]

    def get_left_edge(self):
        return [line[0] for line in self.tile]

    def get_top_edge(self):
        return self.tile[0].copy()

    # should this be a propertie instead?
    def get_bottom_edge(self):
        return self.tile[len(self.tile) - 1].copy()

    def get_edges(self):
        edges = []

        # return list of top, bottom, left, right edges
        edges.append(self.get_top_edge())
        edges.append(self.get_bottom_edge())
        edges.append(self.get_left_edge())
        edges.append(self.get_right_edge())

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

    def rotate_clockwise(self):
        self.tile.reverse()

        # Here, zip does a transpose
        self.tile = list(zip(*self.tile))

        # convert tuple list to list list
        self.tile = [list(i) for i in self.tile]

    def reflect(self):
        # Here, zip does a transpose
        # equivalent to flip across diagonal
        # * unpacks the list, makes all seperate arguments
        self.tile = list(zip(*self.tile))

        # convert tuple list to list list
        self.tile = [list(i) for i in self.tile]

    # Here, get edge is a function
    # e.g. get_left_edge etc
    def make_side_edge(self, edge, get_edge):
        # First, rotate 4 times, see if match
        for _ in range(4):
            self.rotate_clockwise()

            if edge == get_edge():
                return

        # Then reflect, and rotate 4 times again
        self.reflect()
        for _ in range(4):
            self.rotate_clockwise()

            if edge == get_edge():
                return

        # If still here, somthing gone wrong
        raise Exception

    def make_left_edge(self, edge):
        self.make_side_edge(edge, self.get_left_edge)

    def make_top_edge(self, edge):
        self.make_side_edge(edge, self.get_top_edge)

    # Get rid of the boader
    def no_border(self):
        no_border = self.tile

        # remove top and bottom
        no_border = no_border[1 : len(no_border) - 1]

        # remove left and right boarder
        no_border = [row[1 : len(row) - 1] for row in no_border]

        return no_border


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

    def find_matching_tile(self, edge, input_tile, tiles):
        for tile in tiles:
            if tile == input_tile:
                pass
            elif tile.does_edge_match_tile(edge):
                return tile
        return None

    def get_corners(self):
        corners = []
        for tile in self.tiles:
            num_neigh = 0

            for edge in tile.get_edges():
                if (self.find_matching_tile(edge, tile, self.tiles)) != None:
                    num_neigh += 1

            if num_neigh == 2:
                corners.append(tile)
        return corners

    def get_top_left(self):
        corners = self.get_corners()

        top_corner = corners[0]

        # We want this to be the top left corner
        # Rotate the corner as required
        right_match = self.find_matching_tile(
            top_corner.get_right_edge(), top_corner, self.tiles
        )
        bottom_match = self.find_matching_tile(
            top_corner.get_bottom_edge(), top_corner, self.tiles
        )
        while (right_match == None) or (bottom_match == None):
            top_corner.rotate_clockwise()

            right_match = self.find_matching_tile(
                top_corner.get_right_edge(), top_corner, self.tiles
            )
            bottom_match = self.find_matching_tile(
                top_corner.get_bottom_edge(), top_corner, self.tiles
            )
        return top_corner

    def arrange_tiles(self):
        # create blank final output
        side_len = int(math.sqrt(len(self.tiles)))
        arranged_tiles = [[None for j in range(side_len)] for i in range(side_len)]

        # Store unmatched tiles to prevent trying to match
        # already matched tiles (saves computing)
        # only want shallow copy here
        unmatched_tiles = self.tiles.copy()

        # Start with the top corner
        top_corner = self.get_top_left()

        arranged_tiles[0][0] = top_corner
        unmatched_tiles.remove(top_corner)

        # Now scan left to right and solve
        for row_index, row in enumerate(arranged_tiles):
            for col_index in range(len(row)):

                #  If Trying to get left most tile on row, need
                # special treatment
                if col_index == 0:
                    if row[col_index] == None:
                        above_tile = arranged_tiles[row_index - 1][col_index]
                        edge_to_match = above_tile.get_bottom_edge()

                        # find the matching tile
                        match_tile = self.find_matching_tile(
                            edge_to_match, above_tile, unmatched_tiles
                        )

                        # Flip the tile to the correct orientation
                        match_tile.make_top_edge(edge_to_match)

                    else:
                        # already done, must be top left
                        continue

                # Not finding far left tile, just find the tile
                # that matches the right edge of the tile to the
                # left of it
                else:
                    left_tile = row[col_index - 1]
                    edge_to_match = left_tile.get_right_edge()

                    # find the matching tile
                    match_tile = self.find_matching_tile(
                        edge_to_match, left_tile, unmatched_tiles
                    )

                    # Flip the tile to the correct orientation
                    match_tile.make_left_edge(edge_to_match)

                # Save
                row[col_index] = match_tile
                unmatched_tiles.remove(match_tile)

        self.arranged_tiles = arranged_tiles

    def combind_tiles(self):
        # Go through all tiles, remove border
        # and save output in one larger tile
        combind_tiles = []

        # For rows we combind then
        # like this:
        # [[1, 2],
        #  [3, 4]]
        # and
        # [[5, 6],
        #  [7, 8]]
        #
        # becomes:
        # [[1, 2],
        #  [3, 4],
        #  [5, 6],
        #  [7, 8]]
        for row in self.arranged_tiles:

            row_comb = None
            # For tiles in rows, we combind then
            # like this:
            # [[1, 2],
            #  [3, 4]]
            # and
            # [[5, 6],
            #  [7, 8]]
            #
            # becomes:
            # [[1, 2, 5, 6],
            #  [3, 4, 7, 8]]
            for tile in row:
                if row_comb == None:
                    row_comb = tile.no_border()
                else:
                    tile_add = tile.no_border()
                    for i in range(len(row_comb)):
                        row_comb[i] += tile_add[i]

            combind_tiles.extend(row_comb)
        return combind_tiles


class FullImage:
    def __init__(self, data):
        self.data = data
        self.monster = [
            [
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                "#",
                " ",
            ],
            [
                "#",
                " ",
                " ",
                " ",
                " ",
                "#",
                "#",
                " ",
                " ",
                " ",
                " ",
                "#",
                "#",
                " ",
                " ",
                " ",
                " ",
                "#",
                "#",
                "#",
            ],
            [
                " ",
                "#",
                " ",
                " ",
                "#",
                " ",
                " ",
                "#",
                " ",
                " ",
                "#",
                " ",
                " ",
                "#",
                " ",
                " ",
                "#",
                " ",
                " ",
                " ",
            ],
        ]

    def rotate_clockwise(self):
        self.data.reverse()

        # Here, zip does a transpose
        self.data = list(zip(*self.data))

        # convert tuple list to list list
        self.data = [list(i) for i in self.data]

    def reflect(self):
        # Here, zip does a transpose
        # equivalent to flip across diagonal
        # * unpacks the list, makes all seperate arguments
        self.data = list(zip(*self.data))

        # convert tuple list to list list
        self.data = [list(i) for i in self.data]

    def find_sea_monster_data(self):
        # sea monster will be in 20 by 3 frame, look
        # through all the frames in the data:
        for row_index in range(len(self.data)):
            for col_index in range(len(self.data[row_index])):
                # Check for monster
                try:
                    is_monster = True
                    for i in range(len(self.monster)):
                        for j in range(len(self.monster[i])):
                            if (self.monster[i][j] == "#") and (
                                self.data[row_index + i][col_index + j] != "#"
                            ):
                                is_monster = False
                                break
                    if not is_monster:
                        continue

                    # Monster must be here, replace it with "O"
                    for i in range(len(self.monster)):
                        for j in range(len(self.monster[i])):
                            if self.monster[i][j] == "#":
                                assert self.data[row_index + i][col_index + j] == "#"
                                self.data[row_index + i][col_index + j] = "O"

                except IndexError:
                    # No monster
                    continue

    # Loop through all orientations
    def find_all_sea_monster(self):
        # First, rotate 4 times, see if match
        for _ in range(4):
            self.rotate_clockwise()
            self.find_sea_monster_data()

        # Then reflect, and rotate 4 times again
        self.reflect()
        for _ in range(4):
            self.rotate_clockwise()
            self.find_sea_monster_data()

    def count_rough_waters(self):
        count = 0
        for row in self.data:
            for pixel in row:
                if pixel == "#":
                    count += 1

        return count


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

    full_image = FullImage(image.combind_tiles())
    full_image.find_all_sea_monster()
    return full_image.count_rough_waters()


if __name__ == "__main__":
    input = get_input(PATH + "test_input")
    print(part2_solve(input))

    input = get_input(PATH + "real_input")
    print(part2_solve(input))
