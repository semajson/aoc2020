import re
import sys
from dataclasses import dataclass
import math

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day14/"

# Part 1
def apply_mask(mask, value):
    padding = "0" * (len(mask) - len(value))
    value = padding + value

    value = list(value)

    for i in range(len(mask)):
        if mask[i] != "X":
            value[i] = mask[i]

    return "".join(value)


# part 2


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def apply_mask_to_mem_addr(mask, mem_addr):
    padding = "0" * (len(mask) - len(mem_addr))
    mem_addr = padding + mem_addr

    mem_addr = list(mem_addr)

    # apply mask
    for i in range(len(mask)):
        if (mask[i] == "1") or (mask[i] == "X"):
            mem_addr[i] = mask[i]

    # Now deal with all these Xs
    # For each X, create a new mem address, one
    # where the X equals 0 and one where it equals 1
    output = [""]
    for bit in mem_addr:
        if bit == "X":
            zero_value = output.copy()
            zero_value = [addr + "0" for addr in zero_value]

            one_value = output.copy()
            one_value = [addr + "1" for addr in one_value]

            output = zero_value + one_value

        else:
            output = [addr + bit for addr in output]

    return ["".join(addr) for addr in output]


def binary_to_dec(number):
    # dec = int(number)
    return int(number, 2)


def dec_to_binary(number):
    return bin(int(number)).replace("0b", "")


def part1_solve(program):
    memory = {}
    current_mask = None

    for line in program:
        if line.startswith("mask"):
            current_mask = line.replace("mask = ", "")
        else:
            line = line.replace("mem[", "")
            memory_pos, value = line.split("] = ")
            memory_addrs = apply_mask_to_mem_addr(
                current_mask, dec_to_binary(memory_pos)
            )
            for memory_addr in memory_addrs:
                memory[str(binary_to_dec(memory_addr))] = value

    sum = 0

    for memory_pos, value in memory.items():
        sum += int(value)
    return sum


if __name__ == "__main__":

    input = get_input(PATH + "test_input_1")
    print(part1_solve(input))

    input = get_input(PATH + "real_input")
    print(part1_solve(input))
