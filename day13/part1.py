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
    buses = []

    buses_input = input
    buses_input = buses_input[0].split(",")

    for bus in buses_input:
        if bus == "x":
            continue
        buses.append(Bus(bus_no=bus, period=bus, first_leave=0))

    return time_now, buses


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


def part1_solve(time_now, busses):
    first_bus = None
    first_leave_time = None

    for bus in busses:
        leave_time = bus.time_to_next_bus(time_now)

        if (first_bus == None) or (first_leave_time > leave_time):
            first_bus = bus
            first_leave_time = leave_time

    return first_leave_time * first_bus.bus_no


if __name__ == "__main__":

    time_now, buses = parse_input(get_input(PATH + "test_input"))
    print(part1_solve(time_now, buses))

    time_now, buses = parse_input(get_input(PATH + "real_input"))
    print(part1_solve(time_now, buses))
