import re
import sys
from dataclasses import dataclass
import math

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day16/"

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


@dataclass
class Limit:
    lower_limit: int
    upper_limit: int

    def valid_value(self, value):
        if (value >= self.lower_limit) and (value <= self.upper_limit):
            return True
        else:
            return False


@dataclass
class Field:
    name: str
    limits: list = None

    # Is this bad practice, should this be a proper class?
    def valid_value(self, value):
        for limit in self.limits:
            if limit.valid_value(value):
                return True
        return False


def parse_input(input):
    line = input.pop(0)

    fields = []
    my_ticket = None
    nearby_tickets = []

    # first get the fields
    while line != "":
        line = line.replace(" or ", " : ")
        line = line.split(":")
        field = Field(name=line.pop(0))

        # Now parse limits
        for limit in line:
            limit = limit.split("-")
            if field.limits == None:
                field.limits = []
            field.limits.append(
                Limit(lower_limit=int(limit[0]), upper_limit=int(limit[1]))
            )

        fields.append(field)
        # move to next line
        line = input.pop(0)

    # get my ticket
    line = input.pop(0)
    assert line == "your ticket:"
    my_ticket_raw = input.pop(0)
    my_ticket = my_ticket_raw.split(",")
    my_ticket = [int(field) for field in my_ticket]

    # Move past blank line
    line = input.pop(0)

    # get other peoples tickets
    line = input.pop(0)
    assert line == "nearby tickets:"
    nearby_tickets = [line.split(",") for line in input]
    nearby_tickets = [[int(i) for i in ticket] for ticket in nearby_tickets]

    return fields, my_ticket, nearby_tickets


def valid_for_any_field(value, fields):
    for field in fields:
        if field.valid_value(value):
            return True
    return False


def part1_solve(fields, my_ticket, nearby_tickets):

    invalid_field_values = []

    for ticket in nearby_tickets:
        for field_value in ticket:
            if not valid_for_any_field(field_value, fields):
                invalid_field_values.append(field_value)

    return sum(invalid_field_values)


if __name__ == "__main__":

    fields, my_ticket, nearby_tickets = parse_input(get_input((PATH + "test_input")))
    print(part1_solve(fields, my_ticket, nearby_tickets))

    fields, my_ticket, nearby_tickets = parse_input(get_input((PATH + "real_input")))
    print(part1_solve(fields, my_ticket, nearby_tickets))
