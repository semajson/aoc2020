import re
import sys
from dataclasses import dataclass
import math
import copy

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day23/"

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def parse_input(input):
    cups = []
    for cup in input[0]:
        cups.append(int(cup))

    return CupGame(cups)


class CupGame:
    def __init__(self, cups):
        self.cups = cups
        self.cups_min = min(cups)
        self.cups_max = max(cups)

        self.curr_cup_index = int(0)
        self.num_pick_up = 3

    def do_move(self):
        # Pick up the 3 cups after current cup
        cups_to_move = self.cups[
            self.curr_cup_index + 1 : (self.curr_cup_index + 1 + self.num_pick_up)
        ]
        del self.cups[
            self.curr_cup_index + 1 : self.curr_cup_index + 1 + self.num_pick_up
        ]

        # Get destination cup index
        dest_cup = self.cups[self.curr_cup_index] - 1
        while dest_cup not in self.cups:
            dest_cup -= 1
            if dest_cup < self.cups_min:
                dest_cup = self.cups_max

        dest_cup_index = self.cups.index(dest_cup)

        # Insert the cups after the destination cup
        self.cups = (
            self.cups[: dest_cup_index + 1]
            + cups_to_move
            + self.cups[dest_cup_index + 1 :]
        )

        # If destination index was before the current index, rotate list
        # back by 3.
        # We could have also just increased self.curr_cup_index by 3, but
        # this matches the AOC docs so is easier to debug
        # if dest_cup_index < self.curr_cup_index:
        #     for _ in range(3):
        #         self.cups.append(self.cups.pop(0))

        # increase index
        self.cups.append(self.cups.pop(0))
        # self.curr_cup_index += 1
        # if self.curr_cup_index == len(self.cups):
        #     self.curr_cup_index = 0

    def play(self, num_moves=100):
        for _ in range(num_moves):
            self.do_move()

    def get_cups_after_one(self):
        output = ""
        one_index = self.cups.index(1)

        index = one_index + 1
        for _ in range(len(self.cups) - 1):
            output += str(self.cups[index])

            index += 1
            if index == len(self.cups):
                index = 0
        return output


def part1_solve(game):
    game.play(100)
    return game.get_cups_after_one()


if __name__ == "__main__":
    input = parse_input(get_input(PATH + "test_input"))
    print(part1_solve(input))

    input = parse_input(get_input(PATH + "real_input"))
    print(part1_solve(input))
