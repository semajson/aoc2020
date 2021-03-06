import sys, re

sys.path.append("./..")
from utils import time_algo

# Part 1

# use classes more here


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


def valid_number(year, length, max, min):
    if (len(year) != length) or (int(year) > max) or (int(year) < min):
        return False
    return True


def is_passport_valid(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    # print(passport)

    for field in required_fields:
        if field not in passport.keys():
            return False

    # Check the fields
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if not valid_number(
        passport["byr"],
        length=4,
        min=1920,
        max=2002,
    ):
        # print("birth invalid")
        return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020
    if not valid_number(passport["iyr"], length=4, min=2010, max=2020):
        # print("issue invalid")
        return False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not valid_number(passport["eyr"], length=4, min=2020, max=2030):
        # print("expire invalid")
        return False

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    height = passport["hgt"]
    number = height[:-2]
    units = height[len(height) - 2 :]
    if units == "cm":
        if not valid_number(
            number,
            length=3,
            min=150,
            max=193,
        ):
            # print("cm  invalid")
            return False
    elif units == "in":
        if not valid_number(number, length=2, min=59, max=76):
            # print("inch invalid invalid")
            return False
    else:
        # print("no units found invalid")
        return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    reg = re.compile("^[a-f0-9]+\Z")
    if (passport["hcl"][0] != "#") or (
        not bool(reg.match(passport["hcl"][1:])) or len(passport["hcl"][1:]) != 6
    ):
        # print("hair inavlid")
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        # print("ecl inavlid")
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if not valid_number(passport["pid"], length=9, min=-1, max=999999999):
        # print("pid inavlid")
        return False

    # cid (Country ID) - ignored, missing or not.

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
    test_valid = get_input("test_valid")
    test_invalid = get_input("test_invalid")

    print("for valid: ", part1_solve(parse_input(test_valid)))
    print("for invalid: ", part1_solve(parse_input(test_invalid)))
    print("for real: ", part1_solve(parse_input(real_input)))
