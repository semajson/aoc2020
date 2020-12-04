import sys

sys.path.append("./..")
from utils import time_algo

# Part 2


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def count_tree(input, x_increase, y_increase):
    repeat_length = len(input[0])
    tree_count = 0

    run_length = len(input)

    x_pos = 0
    y_pos = 0

    while y_pos < run_length:
        if input[y_pos][x_pos % repeat_length] == "#":
            # print("tree")
            tree_count += 1
        else:
            # print("no tree")
            pass

        x_pos += x_increase
        y_pos += y_increase
    return tree_count


def part1_solve(input):

    repeat_length = len(input[0])


if __name__ == "__main__":

    test_input = get_input("test_input")
    print(test_input)
    real_input = get_input("real_input")

    print(
        count_tree(real_input, 1, 1)
        * count_tree(real_input, 3, 1)
        * count_tree(real_input, 5, 1)
        * count_tree(real_input, 7, 1)
        * count_tree(real_input, 1, 2)
    )
