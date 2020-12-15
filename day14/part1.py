import re
import sys
from dataclasses import dataclass
import math

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day14/"

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def apply_mask(mask, value):
    padding = "0" * (len(mask) - len(value))
    value = padding + value

    value = list(value)

    for i in range(len(mask)):
        if mask[i] != "X":
            value[i] = mask[i]

    return "".join(value)


def binary_to_dec(number):
    # dec = int(number)
    return int(number, 2)


def dec_to_binary(number):
    return bin(int(number)).replace("0b", "")


def part1_solve(program):
    memory = {}
    current_mask = None

    for line in program:
        if line.startswith("mask"):
            current_mask = line.replace("mask = ", "")
        else:
            line = line.replace("mem[", "")
            memory_pos, value = line.split("] = ")
            memory[memory_pos] = apply_mask(current_mask, dec_to_binary(value))

    sum = 0

    for memory_pos, value in memory.items():
        sum += binary_to_dec(value)
    return sum


if __name__ == "__main__":

    input = get_input(PATH + "test_input")
    print(part1_solve(input))

    input = get_input(PATH + "real_input")
    print(part1_solve(input))
