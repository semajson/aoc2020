import sys

sys.path.append("./..")
from utils import time_algo

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def convert_binary_str_to_num(data, zero_char, one_char):

    number = 0
    for i in range(len(data)):
        if data[i] == one_char:
            number += 2 ** (len(data) - i - 1)
        elif data[i] == zero_char:
            pass
        else:
            assert False

    return number


def calc_seat_pos(boarding_pass):
    print("boarding_pass code is: ", boarding_pass)

    # Find row
    row_data = boarding_pass[:7]
    row = convert_binary_str_to_num(row_data, zero_char="F", one_char="B")

    # print("row is: ", row)

    # Find colum
    col_data = boarding_pass[-3:]
    col = convert_binary_str_to_num(col_data, zero_char="L", one_char="R")
    # print("col is: ", col)

    return [row, col]


def calc_seat_id(seat_pos):
    row, column = seat_pos
    return (row * 8) + column


def part1_solve(boarding_passes):
    pos_list = []
    id_list = []

    for boarding_pass in boarding_passes:
        seat_pos = calc_seat_pos(boarding_pass)
        pos_list.append(seat_pos)

        seat_id = calc_seat_id(seat_pos)
        id_list.append(seat_id)

    return max(id_list)


if __name__ == "__main__":

    test_input = get_input("test_input")
    real_input = get_input("real_input")

    """
    for passport in parse_input(test_input):
        print(passport)
    """

    print(part1_solve((real_input)))
