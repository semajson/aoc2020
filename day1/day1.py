import sys

sys.path.append("./..")
from utils import time_algo

# Part 1


def part1_solve_puzzle_set(input, target=2020):
    # Think this is O(n) ...
    set_input = set(input)

    for x in input:
        if (target - x) in set_input:
            print("These numbers solve problem: ", x, target - x)
            return (target - x) * x

    return 0


def part1_solve_puzzle(input, target=2020):
    # Think this is O(n^2)
    for x in input:
        if (target - x) in input:
            # print("These numbers solve problem: ", x, target - x)
            return (target - x) * x

    return 0


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [int(line.rstrip()) for line in content]


if __name__ == "__main__":

    real_input = get_input("input1")
    # test_input = get_input("test_input")

    time_algo(part1_solve_puzzle, real_input, 2020)
    time_algo(part1_solve_puzzle_set, real_input, 2020)

    print(part1_solve_puzzle_set(real_input, 2020))
