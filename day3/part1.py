import sys

sys.path.append("./..")
from utils import time_algo

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def part1_solve(input):
    tree_count = 0
    repeat_length = len(input[0])

    x_pos = 0
    for row in input:
        # print(row)
        if row[x_pos % repeat_length] == "#":
            # print("tree")
            tree_count += 1
        else:
            # print("no tree")
            pass

        x_pos += 3
    return tree_count


if __name__ == "__main__":

    test_input = get_input("test_input")
    real_input = get_input("real_input")

    print(part1_solve(real_input))
