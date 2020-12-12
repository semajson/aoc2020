import re
import sys
from dataclasses import dataclass
import copy

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day11/"


## Might make sense to re-write this using the seat as an object?

# Part 1
def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [list(line.rstrip()) for line in content]


@dataclass
class SurrSeats:
    empty_count: 0
    occ_count: 0
    floor_count: 0

    def update_count(self, seat):
        if seat == "#":
            self.occ_count += 1
        elif seat == "L":
            self.empty_count += 1
        elif seat == ".":
            self.floor_count += 1
        else:
            assert False


def get_surr_seats(row, col, seats):
    surr_seats = SurrSeats(empty_count=0, occ_count=0, floor_count=0)

    for surr_row in range(row - 1, row + 2):
        for surr_col in range(col - 1, col + 2):
            # print("surr_row", surr_row)
            # print("row_row", surr_col)

            if (surr_row == row) and (surr_col == col):
                # this is the current seat, ignore
                continue
            if (surr_row < 0) or (surr_col < 0):
                continue
            try:
                surr_status = seats[surr_row][surr_col]
                surr_seats.update_count(surr_status)

            except IndexError:
                # Must be the wall, just pass
                pass

    return surr_seats


def update_seat_status(row, col, seats):
    status = seats[row][col]

    surr_seats = get_surr_seats(row, col, seats)

    if status == "#" and (surr_seats.occ_count >= 4):
        status = "L"

    elif status == "L" and (surr_seats.occ_count == 0):
        status = "#"

    elif status == ".":
        pass
    else:
        pass

    return status


def updates_all_seats_status(seats):
    seats_changed = 0

    new_seats = copy.deepcopy(seats)

    for i in range(len(seats)):
        for j in range(len(seats[i])):
            prev_status = seats[i][j]
            new_seats[i][j] = update_seat_status(i, j, seats)

            if prev_status != new_seats[i][j]:
                seats_changed = 1

    return seats_changed, new_seats


def part1_solve(seats):

    seats_changed, seats = updates_all_seats_status(seats)

    while seats_changed != 0:
        seats_changed, seats = updates_all_seats_status(seats)

    # Now stable, count the seats
    count = 0
    for row in seats:
        for seat in row:
            if seat == "#":
                count += 1
    return count


if __name__ == "__main__":

    test_input = get_input(PATH + "test_input")
    print(part1_solve(test_input))

    real_input = get_input(PATH + "real_input")
    print(part1_solve(real_input))
