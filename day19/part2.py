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

    # print("42 is: ", resolved_rules["42"])
    # print("11 is: ", resolved_rules["11"])
    # print("31 is: ", resolved_rules["31"])

    return resolved_rules


def part1_solve(rules, messages):
    rules = resolve_rules(rules)

    # print("42 is: ", rules["42"])
    # print("11 is: ", rules["11"])
    # print("31 is: ", rules["31"])

    count = 0

    for message in messages:
        # 0
        if message in rules["0"]:
            count += 1
        # elif message[: len(rules["42"][0])] in rules["42"]:
        #     print("in here")
        #     print("42 len is: ", len(rules["42"][0]))
        #     print("message is ", message)
        #     print("message len is: ", len(message))
        #     print("looking for: ", message[len(rules["42"][0]) :])
        #     print("looking for len is: ", len(message[len(rules["42"][0]) :]))
        #     count += 1
        # 42 0
        elif (message[: len(rules["42"][0])] in rules["42"]) and (
            message[len(rules["42"][0]) :] in rules["0"]
        ):
            count += 1
            # print(message)
        # 42 42 0
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (message[2 * len(rules["42"][0]) :] in rules["0"])
        ):
            count += 1
            # print(message)
        # 42 42 42 0
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (
                message[len(rules["42"][0] * 2) : 3 * len(rules["42"][0])]
                in rules["42"]
            )
            and (message[3 * len(rules["42"][0]) :] in rules["0"])
        ):
            count += 1
            # print(message)
        # 42 42 42 42 0
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (
                message[len(rules["42"][0] * 2) : 3 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[len(rules["42"][0] * 3) : 4 * len(rules["42"][0])]
                in rules["42"]
            )
            and (message[4 * len(rules["42"][0]) :] in rules["0"])
        ):
            count += 1
            # print(message)
        # 42 42 42 42 42 0
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (
                message[len(rules["42"][0] * 2) : 3 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[len(rules["42"][0] * 3) : 4 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[len(rules["42"][0] * 4) : 5 * len(rules["42"][0])]
                in rules["42"]
            )
            and (message[5 * len(rules["42"][0]) :] in rules["0"])
        ):
            count += 1
        # 42 42 42 42 42 42 0
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (
                message[len(rules["42"][0] * 2) : 3 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[len(rules["42"][0] * 3) : 4 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[len(rules["42"][0] * 4) : 5 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[len(rules["42"][0] * 5) : 6 * len(rules["42"][0])]
                in rules["42"]
            )
            and (message[6 * len(rules["42"][0]) :] in rules["0"])
        ):
            count += 1
        # 42 42 42 42 42 42 42 0
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (
                message[len(rules["42"][0] * 2) : 3 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[len(rules["42"][0] * 3) : 4 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[len(rules["42"][0] * 4) : 5 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[len(rules["42"][0] * 5) : 6 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[len(rules["42"][0] * 6) : 7 * len(rules["42"][0])]
                in rules["42"]
            )
            and (message[7 * len(rules["42"][0]) :] in rules["0"])
        ):
            count += 1
            # print(message)
        # elif message[: len(rules["42"][0])] in rules["42"]:
        #     print("in here")
        #     print("31 len is: ", len(rules["31"][0]))
        #     print("message is ", message)
        #     print("message len is: ", len(message))
        #     print("42 len is: ", len(rules["42"][0]))
        #     print(
        #         "looking for: ",
        #         message[len(rules["42"][0]) : len(message) - len(rules["31"][0])],
        #     )
        #     print(
        #         "looking for len is: ",
        #         len(message[len(rules["42"][0]) : len(message) - len(rules["31"][0])]),
        #     )
        #  42 0 31
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[-len(rules["31"][0]) :] in rules["31"])
            and (
                message[len(rules["42"][0]) : len(message) - len(rules["31"][0])]
                in rules["0"]
            )
        ):
            count += 1
            # print(message)

        #  42 42 0 31
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (message[-len(rules["31"][0]) :] in rules["31"])
            and (message[len(rules["42"][0]) * 2 : -len(rules["31"][0])] in rules["0"])
        ):
            count += 1
            # print(message)
        #  42 42 42 0 31
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (
                message[len(rules["42"][0]) * 2 : 3 * len(rules["42"][0])]
                in rules["42"]
            )
            and (message[-len(rules["31"][0]) :] in rules["31"])
            and (message[len(rules["42"][0]) * 3 : -len(rules["31"][0])] in rules["0"])
        ):
            count += 1
            # print(message)
        #  42 42 42 42 0 31
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (
                message[len(rules["42"][0]) * 2 : 3 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[len(rules["42"][0]) * 3 : 4 * len(rules["42"][0])]
                in rules["42"]
            )
            and (message[-len(rules["31"][0]) :] in rules["31"])
            and (message[len(rules["42"][0]) * 4 : -len(rules["31"][0])] in rules["0"])
        ):
            count += 1

        #  42 42 42 42 42 0 31
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (
                message[len(rules["42"][0]) * 2 : 3 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[len(rules["42"][0]) * 3 : 4 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[len(rules["42"][0]) * 4 : 5 * len(rules["42"][0])]
                in rules["42"]
            )
            and (message[-len(rules["31"][0]) :] in rules["31"])
            and (message[len(rules["42"][0]) * 5 : -len(rules["31"][0])] in rules["0"])
        ):
            count += 1
            # print(message)

        #  42 42 0 31 31
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (message[-len(rules["31"][0]) :] in rules["31"])
            and (
                message[-len(rules["31"][0]) * 2 : -len(rules["31"][0])] in rules["31"]
            )
            and (
                message[len(rules["42"][0]) * 2 : -2 * len(rules["31"][0])]
                in rules["0"]
            )
        ):
            count += 1
            # print(message)

        #   42 42 42 0 31 31
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (
                message[2 * len(rules["42"][0]) : 3 * len(rules["42"][0])]
                in rules["42"]
            )
            and (message[-len(rules["31"][0]) :] in rules["31"])
            and (
                message[-len(rules["31"][0]) * 2 : -len(rules["31"][0])] in rules["31"]
            )
            and (
                message[len(rules["42"][0]) * 3 : -2 * len(rules["31"][0])]
                in rules["0"]
            )
        ):
            count += 1
            # print(message)

        #    42 42 42 42 0 31 31
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (
                message[2 * len(rules["42"][0]) : 3 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[3 * len(rules["42"][0]) : 4 * len(rules["42"][0])]
                in rules["42"]
            )
            and (message[-len(rules["31"][0]) :] in rules["31"])
            and (
                message[-len(rules["31"][0]) * 2 : -len(rules["31"][0])] in rules["31"]
            )
            and (
                message[len(rules["42"][0]) * 4 : -2 * len(rules["31"][0])]
                in rules["0"]
            )
        ):
            count += 1
            # print(message)

        # 42 42 42 0 31 31 31
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (
                message[2 * len(rules["42"][0]) : 3 * len(rules["42"][0])]
                in rules["42"]
            )
            and (message[-len(rules["31"][0]) :] in rules["31"])
            and (
                message[-len(rules["31"][0]) * 2 : -len(rules["31"][0])] in rules["31"]
            )
            and (
                message[-len(rules["31"][0]) * 3 : -len(rules["31"][0]) * 2]
                in rules["31"]
            )
            and (
                message[len(rules["42"][0]) * 3 : -3 * len(rules["31"][0])]
                in rules["0"]
            )
        ):
            count += 1
            # print(message)

        # 42 42 42 42 0 31 31 31
        elif (
            (message[: len(rules["42"][0])] in rules["42"])
            and (message[len(rules["42"][0]) : 2 * len(rules["42"][0])] in rules["42"])
            and (
                message[2 * len(rules["42"][0]) : 3 * len(rules["42"][0])]
                in rules["42"]
            )
            and (
                message[3 * len(rules["42"][0]) : 4 * len(rules["42"][0])]
                in rules["42"]
            )
            and (message[-len(rules["31"][0]) :] in rules["31"])
            and (
                message[-len(rules["31"][0]) * 2 : -len(rules["31"][0])] in rules["31"]
            )
            and (
                message[-len(rules["31"][0]) * 3 : -len(rules["31"][0]) * 2]
                in rules["31"]
            )
            and (
                message[len(rules["42"][0]) * 4 : -3 * len(rules["31"][0])]
                in rules["0"]
            )
        ):
            count += 1
            # print(message)
    return count


if __name__ == "__main__":
    rules, messages = parse_input(get_input(PATH + "test_input"))
    print(part1_solve(rules, messages))

    rules, messages = parse_input(get_input(PATH + "real_input"))
    print(part1_solve(rules, messages))
