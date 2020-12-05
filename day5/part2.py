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
    # print("boarding_pass code is: ", boarding_pass)

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


def part2_solve_set(boarding_passes):
    # This is O(n * 1) average??
    # in worse case, is O(n * n)

    pos_list = []
    seat_ids = []

    for boarding_pass in boarding_passes:
        seat_pos = calc_seat_pos(boarding_pass)
        pos_list.append(seat_pos)

        seat_id = calc_seat_id(seat_pos)
        seat_ids.append(seat_id)

    # Use sets here.
    # Loop through the seat_ids. If seat_id + 1 isn't in the set, record that
    seat_ids_set = set(seat_ids)
    my_seat = []
    for seat_id in seat_ids:
        if (seat_id + 1) not in seat_ids_set:
            my_seat.append(seat_id + 1)

    # We always end up with the last item in the list, so just take the minimum here
    return min(my_seat)


def part2_solve(boarding_passes):
    # This is O(nlog(n))
    # Sorting the list is the bottle neck here
    pos_list = []
    seat_ids = []

    for boarding_pass in boarding_passes:
        seat_pos = calc_seat_pos(boarding_pass)
        pos_list.append(seat_pos)

        seat_id = calc_seat_id(seat_pos)
        seat_ids.append(seat_id)

    # Seat ID uniquely identifies each seat, and is sequential.
    # Sort the list, and look for a space.
    seat_ids.sort()
    my_seat = ""
    for j in range(len(seat_ids)):
        if j < len(seat_ids) - 1:
            current_seat_id = seat_ids[j]
            next_seat_id = seat_ids[j + 1]

            if (current_seat_id + 1) != next_seat_id:
                # print("Found space")
                # print(current_seat_id + 1)
                my_seat = current_seat_id + 1

    return my_seat


if __name__ == "__main__":

    test_input = get_input("test_input")
    real_input = get_input("real_input")

    """
    for passport in parse_input(test_input):
        print(passport)
    """

    time_algo(part2_solve, real_input)

    time_algo(part2_solve_set, real_input)
