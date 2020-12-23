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

                if recursion_count > 0:
                    break
            else:
                if char not in resolved_rules:
                    # Loops are baaaad.....
                    # assert char != rule_num
                    if char == rule_num:
                        recursion_count += 1

                    # not current using the recursive one, so error if in here
                    assert char != rule_num

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
    return resolved_rules


def part2_solve(rules, messages):
    rules = resolve_rules(rules)

    count = 0
    # Rules
    # 0: 8 11
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    #
    # This means, all the solutions will be in the form:
    # (42 * x) (42 31 * y)
    # where x >=1 and y >=1
    # all rules in rules[42] and rules[31] are of length 8
    for message in messages:
        step = len(rules["42"][0])
        # step will be 8 chars for our dataset, but keep it general
        if (len(message) % step) != 0:
            continue

        count_42 = 0
        count_31 = 0
        found_31 = False
        is_match = True

        sections = [message[i : i + step] for i in range(0, len(message), step)]
        for section in sections:
            if (section in rules["42"]) and not found_31:
                count_42 += 1
            elif section in rules["31"]:
                count_31 += 1
                found_31 = True
            else:
                is_match = False

        if is_match and (count_31 < count_42) and (count_31 > 0) and (count_42 > 0):
            count += 1

    return count


if __name__ == "__main__":
    rules, messages = parse_input(get_input(PATH + "test_input"))
    print(part2_solve(rules, messages))

    rules, messages = parse_input(get_input(PATH + "real_input"))
    print(part2_solve(rules, messages))
