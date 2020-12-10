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


def is_infinite_loop(commands):
    commands_completed = []

    index = 0
    accumulator = 0
    while True:
        if index >= len(commands):
            # program has terminated
            return False

        command = commands[index]

        if command in commands_completed:
            # Infinite loop
            return True

        index, accumulator = command.do_command(index, accumulator)
        commands_completed.append(command)

    # Something has gone wrong...
    assert False


def run_commands(commands):
    commands_completed = []

    index = 0
    accumulator = 0

    while index < len(commands):
        # print("index is now: ", index)
        # print("accumulator is now: ", accumulator)

        command = commands[index]

        if command in commands_completed:
            # Infinite loop
            assert False

        index, accumulator = command.do_command(index, accumulator)
        commands_completed.append(command)

    return accumulator


def part2_solve(commands):
    # Loop through all commands
    # If command "jmp", replace with "nop"
    # If command "nop", replace with "jop"
    # If no infinte loop, we have fixed the code!
    for command in commands:
        if command.c_type == "jmp":
            command.c_type = "nop"
            if not is_infinite_loop(commands):
                break
            command.c_type = "jmp"

        if command.c_type == "nop":
            command.c_type = "jmp"

            if not is_infinite_loop(commands):
                break
            command.c_type = "nop"

    # We should have fixed code, now run it
    return run_commands(commands)


def parse_input(input):
    commands = []

    for line in input:
        c_type, c_value = line.split(" ")
        command = Command(c_type, int(c_value))
        commands.append(command)
    return commands


if __name__ == "__main__":

    # print(get_input("test_input"))

    test_input = parse_input(get_input(PATH + "test_input"))
    print(part2_solve(test_input))

    real_input = parse_input(get_input(PATH + "real_input"))
    print(part2_solve(real_input))

    # real_input = parse_input(get_input(PATH + "real_input"))

    # real_input = parse_input(get_input("real_input"))
    # print(part1_solve(real_input))
