import re
import sys

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day9/"

# Part 1
def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [int(line.rstrip()) for line in content]


def is_sum_of_pre_2_num(curr_num, prev_nums):
    prev_nums_sets = set(prev_nums)

    for num in prev_nums:
        if ((curr_num - num) != num) and ((curr_num - num) in prev_nums_sets):
            return True

    return False


def part1_solve(input, pre_len):
    data = input
    for i in range(pre_len, len(data)):
        # print("trying number:", data[i])
        if not is_sum_of_pre_2_num(data[i], data[i - pre_len : i]):
            return data[i]
    return -1


if __name__ == "__main__":

    test_input = get_input(PATH + "test_input")
    print(part1_solve(test_input, pre_len=5))

    real_input = get_input(PATH + "real_input")
    print(part1_solve(real_input, pre_len=25))
