import re
import sys
from dataclasses import dataclass
import math
import copy
from collections import deque

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day23/"

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def parse_input_p1(input):
    cups = []
    for cup in input[0]:
        cups.append(int(cup))

    return CupGame(cups)


def parse_input(input):
    cups = []
    for cup in input[0]:
        cups.append(int(cup))

    extra_cup = max(cups) + 1

    while not (extra_cup > 1000000):
        cups.append(extra_cup)
        extra_cup += 1

    return CupGame(cups)


class CupGame:
    def __init__(self, cups):
        self.cups = deque(cups)
        self.cups_min = min(cups)
        self.cups_max = max(cups)
        self.cups_len = len(cups)

        self.curr_cup_index = int(0)
        self.num_pick_up = 3

    def do_move(self):
        # Pick up the 3 cups after current cup
        # the current cup is always at index 0
        # deque can't take index for pop(), so rotate then leftpop
        cups_to_move = []
        self.cups.rotate(-1)
        for _ in range(self.num_pick_up):
            cups_to_move.append(self.cups.popleft())
        self.cups.rotate(1)

        # Get destination cup index
        dest_cup = self.cups[self.curr_cup_index] - 1
        if dest_cup < self.cups_min:
            dest_cup = self.cups_max

        while dest_cup in cups_to_move:
            dest_cup -= 1
            if dest_cup < self.cups_min:
                dest_cup = self.cups_max

        # THIS is the expensive operation...
        # dest_cup_index = self.cups.rindex(dest_cup)
        self.cups.reverse()
        dest_cup_index = (
            self.cups_len - self.num_pick_up - 1 - self.cups.index(dest_cup)
        )
        self.cups.reverse()

        # Insert the cups after the destination cup
        cups_to_move.reverse()
        for cup in cups_to_move:
            self.cups.insert(dest_cup_index + 1, cup)

        # increase index
        self.cups.rotate(-1)

    def play(self, num_moves=100):
        for _ in range(num_moves):
            if (_ % 100) == 0:
                print("done ", _)
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

    def get_prod_2_cups_after_1(self):
        one_index = self.cups.index(1)

        output = 1

        index = one_index + 1
        for _ in range(2):
            output *= self.cups[index]

            index += 1
            if index == len(self.cups):
                index = 0
        return output


def part1_solve(game):
    game.play(100)
    return game.get_cups_after_one()


def part2_solve(game):
    game.play(10000000)
    return game.get_prod_2_cups_after_1()


if __name__ == "__main__":

    input = parse_input_p1(get_input(PATH + "real_input"))
    print(part1_solve(input))

    input = parse_input(get_input(PATH + "test_input"))
    print(part2_solve(input))

    # input = parse_input(get_input(PATH + "real_input"))
    # print(part2_solve(input))
