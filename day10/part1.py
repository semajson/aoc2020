import re
import sys

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day10/"

# Part 1
def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [int(line.rstrip()) for line in content]


def increment_element_dict(dict, key):
    if (dict != {}) and (dict.get(key)):
        dict[key] += 1
    else:
        dict[key] = 1


def part1_solve(adapters):
    adapters.sort()
    diff_dict = {}

    # add the zero diff
    diff = adapters[0] - 0
    increment_element_dict(diff_dict, str(diff))

    for i in range(len(adapters)):

        if i == (len(adapters) - 1):
            increment_element_dict(diff_dict, "3")
            break

        diff = adapters[i + 1] - adapters[i]
        increment_element_dict(diff_dict, str(diff))

    return diff_dict["1"] * diff_dict["3"]


if __name__ == "__main__":

    test_input = get_input(PATH + "test_input")
    print(part1_solve(test_input))

    real_input = get_input(PATH + "real_input")
    print(part1_solve(real_input))
