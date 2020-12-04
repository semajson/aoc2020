import sys

sys.path.append("./..")
from utils import time_algo

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


class PasswordRule:
    def __init__(self, pos_1, pos_2, letter):
        self.letter = str(letter)
        self.pos_1 = int(pos_1)
        self.pos_2 = int(pos_2)

    def rule_passed(self, password):
        count = 0

        if password[self.pos_1 - 1] == self.letter:
            count += 1

        if password[self.pos_2 - 1] == self.letter:
            count += 1

        if count == 1:
            return True
        else:
            return False


class PasswordToCheck:
    def __init__(self, password, rule1):
        self.password = password
        self.rule1 = rule1


def parse_input(input):
    parsed_input = []
    for line in input:
        line = line.replace(":", "")
        line = line.replace("-", " ").split(" ")
        rule1 = PasswordRule(pos_1=line[0], pos_2=line[1], letter=line[2])
        password_to_check = PasswordToCheck(rule1=rule1, password=line[3])

        parsed_input.append(password_to_check)

    return parsed_input


def part1_solve(input):
    parsed_input = parse_input(input)
    failed_count = 0

    for password_info in parsed_input:
        password = password_info.password
        rule = password_info.rule1

        # print("password is:", password)

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
