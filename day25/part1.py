import re
import sys
from dataclasses import dataclass
import math
import copy

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day25/"

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


@dataclass
class Keys:
    card_pub_key: int
    door_pub_key: int


def parse_input(input):
    card_pub_key = input[0]
    door_pub_key = input[1]
    keys = Keys(int(card_pub_key), int(door_pub_key))
    return keys


def do_loop(value, sub_num):
    value *= sub_num
    value = value % 20201227
    return value


def do_loops(value, sub_num, loops):
    for _ in range(loops):
        value = do_loop(value, sub_num)

    return value


def find_loops(pub_key, sub_num):
    loops = 0
    value = 1
    while True:
        value = do_loop(value, sub_num)
        loops += 1
        if value == pub_key:
            break

    return loops


def get_encrypt_key(keys):
    loops = find_loops(keys.card_pub_key, 7)

    print("loops is:", loops)
    return do_loops(1, keys.door_pub_key, loops)


def part1_solve(keys):
    # card_pub_key = keys.card_pub_key
    return get_encrypt_key(keys)


if __name__ == "__main__":
    input = parse_input(get_input(PATH + "test_input"))
    print(part1_solve(input))

    input = parse_input(get_input(PATH + "real_input"))
    print(part1_solve(input))
