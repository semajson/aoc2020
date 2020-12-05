import sys

sys.path.append("./..")
from utils import time_algo

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def parse_input(input):
    passport_list = []

    current_passport = {}

    for line in input:
        if line == "":
            # Blank line, we have reached a new passport. Save the current one off
            if current_passport != {}:
                passport_list.append(current_passport)
            current_passport = {}
            continue

        fields = line.split(" ")

        for key_value in fields:
            key_value = key_value.split(":")

            key = key_value[0]
            value = key_value[1]

            current_passport[key] = value

    # If have current_passport, add it now
    if current_passport != {}:
        passport_list.append(current_passport)

    return passport_list


def is_passport_valid(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for field in required_fields:
        if field not in passport.keys():
            return False
    return True


def part1_solve(input):
    valid_count = 0
    for passport in input:
        if is_passport_valid(passport):
            valid_count += 1

    return valid_count


if __name__ == "__main__":

    test_input = get_input("test_input")
    real_input = get_input("real_input")

    """
    for passport in parse_input(test_input):
        print(passport)
    """

    print(part1_solve(parse_input(real_input)))
