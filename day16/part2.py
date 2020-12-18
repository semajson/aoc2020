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


def part2_solve(fields, my_ticket, nearby_tickets):

    valid_tickets = []

    # Discard all the invalid tickets found in part 1
    for ticket in nearby_tickets:
        ticket_valid = True
        for field_value in ticket:
            if not valid_for_any_field(field_value, fields):
                ticket_valid = False
        if ticket_valid:
            valid_tickets.append(ticket)

    # For each ticket index, record valid possible fields that all tickets
    # satisfy
    possible_fields_for_indexes = [] * len(my_ticket)
    for i in range(len(my_ticket)):
        possible_fields_for_index = []

        for field in fields:
            possible_field = True
            for ticket in valid_tickets:
                if not field.valid_value(ticket[i]):
                    possible_field = False
                    break
            if possible_field:
                possible_fields_for_index.append(field)

        possible_fields_for_indexes.append(possible_fields_for_index)

    # Now we have the possible fields for each index, try and find
    # the index each field corresponds do
    #
    # Do the following algo:
    # - if one index only has 1 possible field, then that field MUST be
    # for that index.
    # - record this field in final_index_fields
    # - Remove this field as an option for other indexes
    # - repeat, and hope a solution is found...
    final_index_fields = [None] * len(my_ticket)
    found_index_field = True
    while found_index_field:
        found_index_field = False
        for i in range(len(possible_fields_for_indexes)):
            if len(possible_fields_for_indexes[i]) == 1:
                found_index_field = True
                resolved_field = possible_fields_for_indexes[i][0]

                # Record this:
                final_index_fields[i] = resolved_field

                # Remove this field now, we have resloved it
                for possible_fields_for_index in possible_fields_for_indexes:
                    if resolved_field in possible_fields_for_index:
                        possible_fields_for_index.remove(resolved_field)

                # Lets start looking through the list again
                break

    # Now do what the question asked, on our ticket find the product of fields
    # with the "departure" in the name
    dep_field_values = []
    for index, field in enumerate(final_index_fields):
        if "departure" in field.name:
            dep_field_values.append(my_ticket[index])

    output = 1
    for value in dep_field_values:
        output *= value

    return output


if __name__ == "__main__":

    fields, my_ticket, nearby_tickets = parse_input(get_input((PATH + "test_input")))
    print(part2_solve(fields, my_ticket, nearby_tickets))

    fields, my_ticket, nearby_tickets = parse_input(get_input((PATH + "real_input")))
    print(part2_solve(fields, my_ticket, nearby_tickets))
