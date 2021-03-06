import re
import sys

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day8/"

# Part 1
def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


class Command:
    def __init__(self, c_type, c_value):
        self.c_type = c_type
        self.c_value = c_value

    def do_command(self, index, accumulator):
        if self.c_type == "nop":
            index += 1
        elif self.c_type == "acc":
            accumulator += self.c_value
            index += 1
        elif self.c_type == "jmp":
            index += self.c_value

        return index, accumulator


def part1_solve(commands):
    commands_completed = []

    index = 0
    accumulator = 0
    while True:
        command = commands[index]

        if command in commands_completed:
            # Completed one loop, break
            break

        index, accumulator = command.do_command(index, accumulator)
        commands_completed.append(command)
    return accumulator


def part1_solve_set(commands):
    commands_completed = set([])

    index = 0
    accumulator = 0
    while True:
        command = commands[index]

        if command in commands_completed:
            # Completed one loop, break
            break

        index, accumulator = command.do_command(index, accumulator)
        commands_completed.add(command)
    return accumulator


def parse_input(input):
    commands = []

    for line in input:
        c_type, c_value = line.split(" ")
        command = Command(c_type, int(c_value))
        commands.append(command)
    return commands


if __name__ == "__main__":

    # print(get_input("test_input"))

    # test_input = parse_input(get_input(PATH + "test_input"))
    # print(part1_solve(test_input))

    real_input = parse_input(get_input(PATH + "real_input"))
    time_algo(part1_solve, real_input)
    time_algo(part1_solve_set, real_input)

    # real_input = parse_input(get_input(PATH + "real_input"))

    part1_solve
