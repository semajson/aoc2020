import re
import sys
from dataclasses import dataclass
import math

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day13/"

# Part 1

# Class here with be ship
#


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def parse_input(input):
    time_now = input.pop(0)
    busses = []

    busses_input = input
    busses_input = busses_input[0].split(",")

    for bus in busses_input:
        if bus == "x":
            busses.append(None)
            continue
        busses.append(Bus(bus_no=bus, period=bus, first_leave=0))

    return time_now, busses


def parse_input_v2(input):
    time_now = input.pop(0)
    busses = []
    offsets = []

    busses_input = input
    busses_input = busses_input[0].split(",")

    for offset in range(len(busses_input)):
        bus = busses_input[offset]
        if bus == "x":
            continue

        busses.append(Bus(bus_no=bus, period=bus, first_leave=0))
        offsets.append(offset)

    return busses, offsets


class Bus:
    def __init__(self, bus_no, period, first_leave):
        self.bus_no = int(bus_no)
        self.period = int(period)
        self.first_leave = int(first_leave)

    def time_to_next_bus(self, time_now):
        time_now = int(time_now)
        last_left = (time_now // self.period) * self.period
        next_leave = last_left + self.period

        return next_leave - time_now

    def __repr__(self):
        return str(self.bus_no)

    def leaves_now(self, time_now):
        time_now = int(time_now)
        if (time_now % self.period) == 0:
            return True
        else:
            return False


def part1_solve(time_now, busses):
    first_bus = None
    first_leave_time = None

    for bus in busses:
        leave_time = bus.time_to_next_bus(time_now)

        if (first_bus == None) or (first_leave_time > leave_time):
            first_bus = bus
            first_leave_time = leave_time

    return first_leave_time * first_bus.bus_no


def part2_solve(bus_order):
    # could brute force, try out numbers, see if the requirement is met
    # could do bit better, rather than loop through all number, could loop
    # through multiples of the first one
    first_bus = bus_order[0]
    first_bus_leave = 0

    while True:
        failure = False
        for x in range(len(bus_order)):
            if bus_order[x] is None:
                pass
            else:
                bus = bus_order[x]
                if not bus.leaves_now(first_bus_leave + x):
                    # this fails
                    failure = True
                    break

        if failure:
            first_bus_leave += first_bus.period
        else:
            break

    return first_bus_leave


def part2_solve_v2(busses, offsets):
    # could we ingore the x by smarter parsing here?
    # have a list of busses, and there offset
    # also, can we increment by the largest bus number?, as I suspect that will cut down
    # time, especially if the largest bus is big

    # looks like this is twice as fast as part v1 only :/

    # get longest period
    longest_period = 0
    diff_first_bus = 0
    for x in range(len(busses)):
        bus = busses[x]
        offest = offsets[x]

        if bus.period > longest_period:
            longest_period = bus.period
            diff_first_bus = offest

    first_bus_leave = 0
    num_longest_period = 0

    while True:
        failure = False
        for x in range(len(busses)):
            bus = busses[x]
            offset = offsets[x]

            if not bus.leaves_now(first_bus_leave + offset):
                # this fails
                failure = True
                break

        if failure:
            num_longest_period += 1
            first_bus_leave = (num_longest_period * longest_period) - diff_first_bus
        else:
            break

    return first_bus_leave


def part2_solve_v3(busses, offsets):
    # Say we have the equations
    # T = 3x
    # Here, T=3 is a solution (here x =1)
    #
    # Now if also
    # T = 1 + 4y
    # The previous answer T= 3 isn't solution, but if find a solution T = a * 3 where a is int
    # where this equation is satisfied, the first equation will still be satisfied
    #
    # Now if also:
    # T = 2 + 5z
    # The we can iterate through T = a * 3 * 4 till we find a solution.
    # Importantly, all the other equations will still be satisfied.
    #
    # So loop through the busses finding a first_bus_leave time that works.
    # Use the product from the previous buses as the "period here".
    # So that the next solutuion we guess is current_period * a where we iterate a
    first_bus_leave = None
    current_period = None

    for x in range(len(busses)):
        bus = busses[x]
        offset = offsets[x]

        if first_bus_leave == None:
            first_bus_leave = bus.period + offset
            current_period = bus.period
        else:

            while (first_bus_leave + offset) % (bus.period) != 0:
                first_bus_leave += current_period
            current_period *= bus.period

    return first_bus_leave


if __name__ == "__main__":

    time_now, busses = parse_input(get_input(PATH + "test_input"))
    print(part2_solve(busses))

    busses, offsets = parse_input_v2(get_input(PATH + "real_input"))
    print(part2_solve_v3(busses, offsets))

    """
    time_now, busses = parse_input(get_input(PATH + "test_input_1"))
    time_algo(part2_solve, busses)

    busses, offsets = parse_input_v2(get_input(PATH + "test_input_1"))
    time_algo(part2_solve_v2, busses, offsets)

    # Trying real
    busses, offsets = parse_input_v2(get_input(PATH + "real_input"))
    print(part2_solve_v2(busses, offsets))
    """
