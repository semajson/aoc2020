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


def get_next_num_v2(numbers):
    last_num = numbers[-1]

    if last_num not in numbers[:-1]:
        return 0
    else:
        last_index = len(numbers) - 1 - 1
        while True:
            if numbers[last_index] == last_num:
                break
            last_index -= 1

        return (len(numbers) - 1) - last_index


def get_next_num_set(numbers, nums_set):
    last_num = numbers[-1]

    if last_num not in nums_set:
        nums_set.add(last_num)
        return 0
    else:
        # maybe re-write this, seems very complex
        # also I suspect it is pretty slow...
        last_index = max(
            [pos for pos, value in enumerate(numbers[:-1]) if value == last_num]
        )

        return (len(numbers) - 1) - last_index


def get_next_num_set_v2(numbers, nums_set):
    last_num = numbers[-1]

    if last_num not in nums_set:
        nums_set.add(last_num)
        return 0
    else:
        last_index = len(numbers) - 1 - 1
        while 1:
            if numbers[last_index] == last_num:
                break
            last_index -= 1

        return (len(numbers) - 1) - last_index


def get_next_num_set_v3(numbers, nums_set):
    last_num = numbers[-1]

    if last_num not in nums_set:
        nums_set.add(last_num)
        return 0
    else:
        numbers.reverse()
        last_index = len(numbers) - numbers.index(last_num, 1) - 1
        numbers.reverse()

        return (len(numbers) - 1) - last_index


def part2_solve(numbers):

    while len(numbers) < 10000:
        next_num = get_next_num(numbers)
        numbers.append(next_num)

    return numbers[-1]


def part2_solve_v2(numbers):

    while len(numbers) < 10000:
        next_num = get_next_num_v2(numbers)
        numbers.append(next_num)

    return numbers[-1]


def part2_solve_set(numbers):

    nums_set = set(numbers[:-1])

    while len(numbers) < 10000:
        next_num = get_next_num_set(numbers, nums_set)
        numbers.append(next_num)

    return numbers[-1]


def part2_solve_set_v2(numbers):

    nums_set = set(numbers[:-1])

    while len(numbers) < 10000:
        next_num = get_next_num_set_v2(numbers, nums_set)
        numbers.append(next_num)

    return numbers[-1]


def part2_solve_set_v3(numbers):

    nums_set = set(numbers[:-1])

    while len(numbers) < 2020:
        next_num = get_next_num_set_v3(numbers, nums_set)
        numbers.append(next_num)

    return numbers[-1]


def get_next_num_dict(numbers, num_dict):
    last_num = numbers[-1]

    if str(last_num) not in num_dict:
        num_dict[str(last_num)] = str(len(numbers) - 1)
        return 0
    else:
        last_used = int(num_dict[str(last_num)])

        num_dict[str(last_num)] = str(len(numbers) - 1)

        return (len(numbers) - 1) - last_used


def part2_solve_dict(numbers):

    num_dict = {}
    for i in range(len(numbers) - 1):
        num_dict[str(numbers[i])] = str(i)

    while len(numbers) < 30000000:
        next_num = get_next_num_dict(numbers, num_dict)
        numbers.append(next_num)

    return numbers[-1]


if __name__ == "__main__":
    """
    input = parse_input(get_input((PATH + "real_input")))
    time_algo(part2_solve, input)

    input = parse_input(get_input((PATH + "real_input")))
    time_algo(part2_solve_v2, input)

    input = parse_input(get_input((PATH + "real_input")))
    time_algo(part2_solve_set, input)
    """
    """
    input = parse_input(get_input((PATH + "real_input")))
    print(part2_solve_set_v3(input))
    """
    # time_algo(part2_solve_set_v3, input)

    # input = parse_input(get_input((PATH + "real_input")))
    # time_algo(part2_solve_set_v2, input)

    # input = parse_input(get_input(PATH + "real_input"))
    # print(part1_solve(input))

    # input = parse_input(get_input((PATH + "test_input")))
    # time_algo(part2_solve_set_v3, input)

    input = parse_input(get_input((PATH + "real_input")))
    print(part2_solve_dict(input))
