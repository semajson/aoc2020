import re
import sys
from dataclasses import dataclass
import math
import copy

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day17/"

# Part 1


class Cube:
    def __init__(self, active=False):

        self.active = active

    def update(self, active_neighs):
        if self.active and ((active_neighs == 2) or (active_neighs == 3)):
            pass
        elif self.active:
            self.active = False
        elif (not self.active) and (active_neighs == 3):
            self.active = True

    def __repr__(self):
        if self.active:
            return "#"
        else:
            return "."


class CubeGrid:
    def __init__(self, initial_plane, cycles):
        self.cycles = cycles

        max_x_planes = len(initial_plane[0]) + (cycles * 2)
        max_y_planes = len(initial_plane) + (cycles * 2)
        max_z_planes = 1 + (cycles * 2)
        max_w_planes = 1 + (cycles * 2)

        # First, create plan planes
        self.grid = [
            [
                [
                    [Cube(active=False) for x in range(max_x_planes)]
                    for y in range(max_y_planes)
                ]
                for z in range(max_z_planes)
            ]
            for w in range(max_w_planes)
        ]

        # Fill in the plane information in the grid
        for y in range(len(initial_plane)):
            for x in range(len(initial_plane[0])):
                if initial_plane[y][x] == "#":
                    w_grid = cycles
                    z_grid = cycles
                    y_grid = cycles + y
                    x_grid = cycles + x
                    cube = self.grid[w_grid][z_grid][y_grid][x_grid]
                    cube.active = True

    def get_active_neighbours(self, x, y, z, w):
        active_neighs = 0
        for w_offset in range(-1, 2):
            for z_offset in range(-1, 2):
                for y_offset in range(-1, 2):
                    for x_offset in range(-1, 2):
                        try:
                            x_neigh = x + x_offset
                            y_neigh = y + y_offset
                            z_neigh = z + z_offset
                            w_neigh = w + w_offset

                            if (
                                (x_neigh < 0)
                                or (y_neigh < 0)
                                or (z_neigh < 0)
                                or (w_neigh < 0)
                            ):
                                raise IndexError

                            if x_offset == y_offset == z_offset == w_offset == 0:
                                # own cell, just ignore
                                continue

                            neigh_cube = self.grid[w_neigh][z_neigh][y_neigh][x_neigh]

                            if neigh_cube.active:
                                active_neighs += 1

                        except IndexError:
                            # Hit a wall, just pass
                            pass

        return active_neighs

    def do_cycle(self):
        new_grid = copy.deepcopy(self.grid)

        for w in range(len(self.grid)):
            for z in range(len(self.grid[0])):
                for y in range(len(self.grid[0][0])):
                    for x in range(len(self.grid[0][0][0])):
                        cube = new_grid[w][z][y][x]
                        active_neighs = self.get_active_neighbours(x, y, z, w)
                        cube.update(active_neighs)

        self.grid = new_grid

    def count_active(self):
        active_count = 0

        for w in range(len(self.grid)):
            for z in range(len(self.grid[0])):
                for y in range(len(self.grid[0][0])):
                    for x in range(len(self.grid[0][0][0])):
                        cube = self.grid[w][z][y][x]
                        if cube.active:
                            active_count += 1

        return active_count


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def create_grid(input):
    initial_plane = [list(row) for row in input]
    cube_grid = CubeGrid(initial_plane=initial_plane, cycles=6)
    return cube_grid


def part1_solve(grid):
    for i in range(6):
        grid.do_cycle()

    return grid.count_active()


if __name__ == "__main__":
    grid = create_grid(get_input(PATH + "test_input"))
    print(part1_solve(grid))

    grid = create_grid(get_input(PATH + "real_input"))
    print(part1_solve(grid))
