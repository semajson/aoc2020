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


def parse_input(seats):
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            seats[row][col] = Seat(status=seats[row][col])
    return seats


@dataclass
class SeatsInfo:
    empty_count: 0
    occ_count: 0
    floor_count: 0

    def update_count(self, seat):
        if seat.is_occ:
            self.occ_count += 1
        elif seat.is_floor:
            self.floor_count += 1
        else:
            self.empty_count += 1


class Seat:
    # Hmm, should the row index and the col index
    # also be internal state of the seat?
    def __init__(self, status):
        self.is_occ = False
        self.is_floor = False
        if status == "#":
            self.is_occ = True
        elif status == "L":
            self.is_occ = False
        elif status == ".":
            self.is_floor = True

        self.char_rep = str(status)

    def update_seat_status(self, row, col, seats):

        view_seats = self.get_view_seats(row, col, seats)

        if self.is_occ and (view_seats.occ_count >= 5):
            self.is_occ = False

        elif (not self.is_occ) and (not self.is_floor) and (view_seats.occ_count == 0):
            self.is_occ = True
        elif self.is_floor:
            pass
        else:
            pass

    def __str__(self):
        return self.char_rep

    def __repr__(self):
        return self.char_rep

    def get_surr_seats(self, row, col, seats):
        surr_seats = SeatsInfo(empty_count=0, occ_count=0, floor_count=0)

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
                    seat = seats[surr_row][surr_col]
                    surr_seats.update_count(seat)

                except IndexError:
                    # Must be the wall, just pass
                    pass

        return surr_seats

    def get_dir_view_seats(self, row, col, dir, seats, view_seats):

        while True:
            row += dir[0]
            col += dir[1]

            if row < 0 or col < 0:
                # Hit wall
                break

            try:
                seat = seats[row][col]

                if not seat.is_floor:
                    view_seats.update_count(seat)
                    break

            except IndexError:
                # hit wall
                break

    def get_view_seats(self, row, col, seats):
        view_seats = SeatsInfo(empty_count=0, occ_count=0, floor_count=0)

        # loop over the possible 8 directions, and get the seats in that view
        for row_dir in range(-1, 2):
            for col_dir in range(-1, 2):

                # Ingore 0,0, this doesn't correspond to a direction
                if (row_dir == 0) and (col_dir == 0):
                    continue
                dir = [row_dir, col_dir]

                self.get_dir_view_seats(row, col, dir, seats, view_seats)

        return view_seats


def updates_all_seats_status(seats):
    seats_changed = 0

    new_seats = copy.deepcopy(seats)

    print(seats)

    for i in range(len(seats)):
        for j in range(len(seats[i])):
            prev_seat = seats[i][j]
            new_seat = new_seats[i][j]

            new_seat.update_seat_status(i, j, seats)

            if prev_seat.is_occ != new_seat.is_occ:
                seats_changed = 1

    return seats_changed, new_seats


def part2_solve(seats):

    seats_changed, seats = updates_all_seats_status(seats)

    while seats_changed != 0:
        seats_changed, seats = updates_all_seats_status(seats)

    # Now stable, count the seats
    count = 0
    for row in seats:
        for seat in row:
            if seat.is_occ:
                count += 1
    return count


if __name__ == "__main__":

    test_input = parse_input(get_input(PATH + "test_input"))
    print(part2_solve(test_input))

    # real_input = parse_input(get_input(PATH + "real_input"))
    # print(part2_solve(real_input))
