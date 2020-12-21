import re
import sys
from dataclasses import dataclass
import math
import copy

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day19/"

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def parse_input(input):
    rules = {}

    # parse out the rules
    line = input.pop(0)
    while line != "":
        index, rule = line.split(": ")
        rules[index] = rule
        line = input.pop(0)

    # We are just left with mesages
    # trim the "" messages here
    messages = input

    return rules, messages


def get_combos(list1, list2):
    combos = []

    if list1 == []:
        return list2

    for i in list1:
        for j in list2:
            new_element = i + j
            if len(new_element) > 100:
                new_element = new_element[:100]
            combos.append(new_element)

    return combos


def resolve_rule(rule_num, resolved_rules, rules, recursion_count):
    if rule_num in resolved_rules:
        return

    rule = rules[rule_num]

    # Special code to handle these pesky loops
    """
    if (rule_num == "8") or (rule_num == "11"):
        base = []
        repeater = []

        rule_command = rule.split(" ")

        current_messages = "left"

        for char in rule_command:
            if char == "|":
                current_messages = "right"
            else:
                if char == rule_num:
                    recursive_messages = base
                    for _ in range(2):
                        recursive_messages += get_combos(recursive_messages, repeater)
                    resolved_rules[rule_num] = recursive_messages
                    return
                else:
                    if char not in resolved_rules:
                        resolve_rule(char, resolved_rules, rules, recursion_count)

                    message = resolved_rules[char]

                    if current_messages == "left":
                        base = get_combos(base, message)
                    else:
                        repeater = get_combos(repeater, message)
    """
    if rule.startswith('"'):
        resolved_rules[rule_num] = [rule[1:-1]]
    else:
        rule_command = rule.split(" ")

        left_messages = []
        right_messages = []

        current_messages = "left"

        for char in rule_command:
            if char == "|":
                current_messages = "right"

                if recursion_count > 1:
                    break
            else:
                if char not in resolved_rules:
                    # Loops are baaaad.....
                    # assert char != rule_num
                    if char == rule_num:
                        recursion_count += 1

                    resolve_rule(char, resolved_rules, rules, recursion_count)

                message = resolved_rules[char]

                if current_messages == "left":
                    left_messages = get_combos(left_messages, message)
                else:
                    right_messages = get_combos(right_messages, message)

        resolved_rules[rule_num] = left_messages + right_messages


def resolve_rules(rules):
    resolved_rules = {}

    for rule_num in rules:
        if rule_num not in resolved_rules:
            resolve_rule(rule_num, resolved_rules, rules, 0)

    # print("42 is: ", resolved_rules["42"])
    # print("11 is: ", resolved_rules["11"])
    # print("31 is: ", resolved_rules["31"])

    return resolved_rules


def part1_solve(rules, messages):
    rules = resolve_rules(rules)

    count = 0
    for message in messages:
        if message in rules["0"]:
            count += 1

    return count


if __name__ == "__main__":
    rules, messages = parse_input(get_input(PATH + "test_input_1"))
    print(part1_solve(rules, messages))

    # rules, messages = parse_input(get_input(PATH + "real_input"))
    # print(part1_solve(rules, messages))
