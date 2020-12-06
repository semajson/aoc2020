import sys

sys.path.append("./..")
from utils import time_algo

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


# Here, each group is a list of each persons results
def parse_input_per_person(input):
    groups = []

    current_group = []

    for line in input:
        if line == "":
            # End of the current group
            groups.append(current_group)
            current_group = []
            continue

        current_group.append(line)

    if current_group != []:
        groups.append(current_group)

    return groups


# Here, each group is combined string of all the results from everyone in the group
def parse_input_comb_group(input):
    groups = []

    current_group = ""

    for line in input:
        if line == "":
            # End of the current group
            groups.append(current_group)
            current_group = ""
            continue

        current_group += line

    if current_group != []:
        groups.append(current_group)

    return groups


def group_contains_all_yes(group, answer):
    for person in group:
        if answer not in person:
            return False
    return True


def group_contains_any_yes(group, answer):
    if answer in group:
        return True
    else:
        return False


def part2_solve(groups):
    # Again, rrder here is O( n * m)
    # where  is number of groups, and m is the number of people in group

    yes_answers = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    any_yes_count = 0

    for group in groups:
        for answer in yes_answers:
            if group_contains_all_yes(group, answer):
                any_yes_count += 1

    return any_yes_count


if __name__ == "__main__":

    test_input = parse_input_per_person(get_input("test_input"))
    real_input = parse_input_per_person(get_input("real_input"))

    print(part2_solve(test_input))
    print(part2_solve(real_input))
