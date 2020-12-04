import sys

sys.path.append("./..")
from utils import time_algo

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


class PasswordRule:
    def __init__(self, lower_limit, upper_limit, letter):
        self.letter = str(letter)
        self.lower_limit = int(lower_limit)
        self.upper_limit = int(upper_limit)

    def rule_passed(self, password):
        letter_count = password.count(self.letter)

        if (letter_count < self.lower_limit) or (self.upper_limit < letter_count):
            return False

        return True


class PasswordToCheck:
    def __init__(self, password, rule1):
        self.password = password
        self.rule1 = rule1


def parse_input(input):
    parsed_input = []
    for line in input:
        line = line.replace(":", "")
        line = line.replace("-", " ").split(" ")
        rule1 = PasswordRule(lower_limit=line[0], upper_limit=line[1], letter=line[2])
        password_to_check = PasswordToCheck(rule1=rule1, password=line[3])

        parsed_input.append(password_to_check)

    return parsed_input


def part1_solve(input):
    parsed_input = parse_input(input)
    failed_count = 0

    for password_info in parsed_input:
        password = password_info.password
        rule = password_info.rule1

        if not rule.rule_passed(password):
            failed_count += 1
            # print("failed")

    return len(input) - failed_count


if __name__ == "__main__":

    test_input = get_input("test_input")
    real_input = get_input("real_input")

    print(part1_solve(real_input))

    # time_algo(part1_solve_puzzle, real_input, 2020)
    # time_algo(part1_solve_puzzle_set, real_input, 2020)

    # print(part1_solve_puzzle_set(real_input, 2020))
