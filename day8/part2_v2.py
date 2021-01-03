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

    def swap_command(self):
        if self.c_type == "jmp":
            self.c_type = "nop"
        elif self.c_type == "nop":
            self.c_type = "jmp"

    def swap_command_back(self):
        # As swap_command is symmetric, just call it again
        self.swap_command()


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
    # Alter command
    # If no infinte loop, we have fixed the code!
    for command in commands:
        command.swap_command()
        if not is_infinite_loop(commands):
            break
        command.swap_command_back()

    # We should have fixed code, now run it
    return run_commands(commands)


def build_moves(steps):
    moves = {}

    for src, dst in steps:
        if src in moves:
            moves[src].append(dst)
        else:
            moves[src] = [dst]
    return moves


# Own original recursive calc moves, just to see how
# it would work...
def readchable_recur(moves, start, visited=None):

    # Can't create default mutable object in the arguments
    # as it will be shared across different function calls
    if visited == None:
        visited = set()

    if start in visited:
        return
    visited.add(start)

    # Visit all the destinations if there are any
    if start not in moves:
        return

    dests = moves[start]

    # Got to deal with forking, use recurision here
    for dest in dests:
        readchable_recur(moves, dest, visited)

    return visited


def reachable(moves, start):

    to_visit = [start]
    visited = set()

    # This while loop (courtesy of TPW) is very clever
    # it deals very nicely with the forking without needing recurision
    while to_visit != []:
        current = to_visit.pop()

        if current in visited:
            continue

        visited.add(current)

        if current not in moves:
            continue
        to_visit.extend(moves[current])

    return visited


def part2_solve_v2(commands):
    # build a map of where each command takes you
    # wherein applying the "source" command takes you to the "destination" command
    steps_fwds = []
    steps_backs = []
    for src_index, command in enumerate(commands):
        dst_index, _ = command.do_command(src_index, 0)
        steps_fwds.append((src_index, dst_index))
        steps_backs.append((dst_index, src_index))

    # Go through the steps and combine them to deal with forking.
    # e.g, multiple commands could take you to a given destination
    forwards = build_moves(steps_fwds)
    backwards = build_moves(steps_backs)

    # Find indexes can reach from start
    reachable_forward = readchable_recur(forwards, 0)

    # Find indexes you get to the end from
    reachable_backwards = readchable_recur(backwards, len(commands))

    # see if flip forward index can get to the reachable backwards path
    for index in reachable_forward:
        commands[index].swap_command()
        new_dest, _ = commands[index].do_command(index, 0)

        if new_dest in reachable_backwards:
            break
        else:
            commands[index].swap_command_back()

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

    # test_input = parse_input(get_input(PATH + "test_input"))
    # print(part2_solve(test_input))

    # real_input = parse_input(get_input(PATH + "real_input"))
    # print(part2_solve(real_input))

    test_input = parse_input(get_input(PATH + "test_input"))
    print(part2_solve_v2(test_input))

    real_input = parse_input(get_input(PATH + "real_input"))
    print(part2_solve_v2(real_input))

    # real_input = parse_input(get_input(PATH + "real_input"))

    # real_input = parse_input(get_input("real_input"))
    # print(part1_solve(real_input))
