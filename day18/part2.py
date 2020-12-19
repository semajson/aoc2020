import re
import sys
from dataclasses import dataclass
import math
import copy

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day18/"

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def parse_input(input):

    return [list(line.replace(" ", "")) for line in input]


def calc_expression(expression):
    operator = ""

    index = 0
    while index < len(expression):
        symbol = expression[index]
        # Check if it is an operator
        if (symbol == "*") or (symbol == "+"):
            operator = symbol
            index += 1
            continue

        # If bracket, work out the value for the expression in bracket
        # first
        if symbol == "(":
            # Find the corresponding closing bracket
            bracket_stack = []
            for close_index in range(index + 1, len(expression)):
                if (expression[close_index] == ")") and (bracket_stack == []):
                    # found closing index
                    break
                elif expression[close_index] == ")":
                    # found 1 close bracket.
                    bracket_stack.pop()
                elif expression[close_index] == "(":
                    bracket_stack.append("(")

            next_number = calc_expression(expression[index + 1 : close_index])
            index = close_index
        else:
            # It must be a number
            next_number = int(symbol)

        if operator == "*":
            number *= next_number
        elif operator == "+":
            number += next_number
        elif operator == "":
            number = next_number

        index += 1

    return number


def add_brackets(expression):
    index = 0
    while index < len(expression):
        if (expression[index] == "+") and (expression[index + 1] != "("):
            expression.insert(index - 1, "(")
            expression.insert(index + 3, ")")
            index += 1
        elif (expression[index] == "+") and (expression[index + 1] == "("):
            # Find the corresponding closing bracket
            bracket_stack = []
            for close_index in range(index + 2, len(expression)):
                if (expression[close_index] == ")") and (bracket_stack == []):
                    # found closing index
                    break
                elif expression[close_index] == ")":
                    # found 1 close bracket.
                    bracket_stack.pop()
                elif expression[close_index] == "(":
                    bracket_stack.append("(")

            expression.insert(index - 1, "(")
            expression.insert(close_index + 1, ")")
            index += 1

        index += 1


# Given no brackets, this will do + first then * next
def calc_bracketless_expression(expression):
    add_brackets(expression)
    return calc_expression(expression)


def build_bracketless_expression(expression):
    operator = ""

    index = 0
    while index < len(expression):
        symbol = expression[index]
        # Check if it is an operator
        if (symbol == "*") or (symbol == "+"):
            operator = symbol
            index += 1
            continue

        # If bracket, work out the value for the expression in bracket
        # first
        if symbol == "(":
            # Find the corresponding closing bracket
            bracket_stack = []
            for close_index in range(index + 1, len(expression)):
                if (expression[close_index] == ")") and (bracket_stack == []):
                    # found closing index
                    break
                elif expression[close_index] == ")":
                    # found 1 close bracket.
                    bracket_stack.pop()
                elif expression[close_index] == "(":
                    bracket_stack.append("(")

            next_number = calc_expression(expression[index + 1 : close_index])
            index = close_index
        else:
            # It must be a number
            next_number = int(symbol)

        if operator == "*":
            number *= next_number
        elif operator == "+":
            number += next_number
        elif operator == "":
            number = next_number

        index += 1

    return number


def part2_solve(expressions):
    sum = 0
    for expression in expressions:
        print(calc_bracketless_expression(expression))

    return sum


if __name__ == "__main__":
    input = parse_input(get_input(PATH + "test_input"))
    print(part2_solve(input))

    # input = parse_input(get_input(PATH + "real_input"))
    # print(part2_solve(input))
