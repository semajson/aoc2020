import re
import sys
from dataclasses import dataclass
import math

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day15/"

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def parse_input(input):
    numbers = input[0].split(",")

    return [int(num) for num in numbers]


def get_next_num(numbers):
    last_num = numbers[-1]

    if last_num not in numbers[:-1]:
        return 0
    else:
        # maybe re-write this, seems very complex
        # also I suspect it is pretty slow...
        last_index = max(
            [pos for pos, value in enumerate(numbers[:-1]) if value == last_num]
        )

        return (len(numbers) - 1) - last_index


def part1_solve(numbers):

    while len(numbers) < 30000000:
        next_num = get_next_num(numbers)
        numbers.append(next_num)

    return numbers[-1]


if __name__ == "__main__":

    input = parse_input(get_input((PATH + "test_input")))
    print(part1_solve(input))

    input = parse_input(get_input(PATH + "real_input"))
    print(part1_solve(input))
