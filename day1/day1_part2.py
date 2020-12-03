import sys
from day1 import part1_solve_puzzle_set

sys.path.append("./..")
from utils import time_algo


# Part 2
def part2_solve_puzzle_set(input, target=2020):
    # Think this is O(n^2) ...

    for x in input:
        new_target = target - x
        new_input = input.copy()
        new_input.remove(x)

        result = part1_solve_puzzle_set(new_input, new_target)
        if result != 0:
            print("x was", x)
            return x * result

    return 0


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [int(line.rstrip()) for line in content]


if __name__ == "__main__":
    real_input = get_input("input1")

    print(part2_solve_puzzle_set(real_input))

    time_algo(part2_solve_puzzle_set, real_input, 2020)