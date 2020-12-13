import sys

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day6/"

# Part 1


# make this more classy


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


class Group:
    def __init__(self, people_ans):
        self.people_ans = people_ans

    def group_contains_all_yes(self, answer):
        for person_ans in self.people_ans:
            if answer not in person_ans:
                return False
        return True

    def group_contains_any_yes(self, answer):
        all_ans = ""
        for person_ans in self.people_ans:
            all_ans += person_ans

        if answer in all_ans:
            return True
        else:
            return False


# Here, each group is a list of each persons results
def parse_input(input):
    groups = []

    current_group = []

    for line in input:
        if line == "":
            # End of the current group
            groups.append(Group(people_ans=current_group))
            current_group = []
            continue

        current_group.append(line)

    if current_group != []:
        groups.append(Group(people_ans=current_group))

    return groups


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
            if group.group_contains_all_yes(answer):
                any_yes_count += 1

    return any_yes_count


if __name__ == "__main__":

    test_input = parse_input(get_input(PATH + "test_input"))
    real_input = parse_input(get_input(PATH + "real_input"))

    print(part2_solve(test_input))
    print(part2_solve(real_input))
