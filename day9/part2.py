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


def part1_solve(data, pre_len):
    for i in range(pre_len, len(data)):
        # print("trying number:", data[i])
        if not is_sum_of_pre_2_num(data[i], data[i - pre_len : i]):
            return data[i]
    return -1


def part2_solve(data, target):

    # Loop through all numbers, if a list contiguous numbers immediately
    # after it add up to the target number, we have found the desired
    # numbers!
    for i in range(len(data)):
        # If this is the target number (which is in the dataset), just skip
        if data[i] == target:
            continue

        current_sum = data[i]
        current_nums = [data[i]]

        for j in range(i + 1, len(data)):
            current_sum += data[j]
            current_nums.append(data[j])

            if current_sum == target:
                return min(current_nums) + max(current_nums)
    # didn't find number
    return -1


if __name__ == "__main__":

    test_input = get_input(PATH + "test_input")
    invalid_num = part1_solve(test_input, pre_len=5)
    print("invalid number is", invalid_num)
    print(part2_solve(test_input, invalid_num))

    real_input = get_input(PATH + "real_input")
    invalid_num = part1_solve(real_input, pre_len=25)
    print("invalid number is", invalid_num)
    print(part2_solve(real_input, invalid_num))
