import re
import sys
from dataclasses import dataclass
import math
import copy
from collections import deque

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day23/"

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


def parse_input_p1(input):
    cups = []
    for cup in input[0]:
        cups.append(int(cup))

    return CupGame(cups)


def parse_input(input):
    cups = []
    for cup in input[0]:
        cups.append(int(cup))

    extra_cup = max(cups) + 1

    while not (extra_cup > 1000000):
        cups.append(extra_cup)
        extra_cup += 1

    return CupGame(cups)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def rotate(self):
        self.head = self.head.next

    def find_node(self, value):
        head_count = 0

        node = self.head
        while head_count < 2:
            if value == node.data:
                return node

            # This is cyclic linked list, so we only want to loop through once
            # achieve this by tracking how often visted head node
            if node == self.head:
                head_count += 1

            node = node.next

        return None

    # Used for debugging, comment out to increase performance
    # def __repr__(self):
    #     nodes = [str(self.head.data)]

    #     node = self.head.next
    #     while node is not self.head:
    #         nodes.append(str(node.data))
    #         node = node.next

    #     nodes.append(str(self.head.data))
    #     return str(" -> ".join(nodes))


class CupGame:
    def __init__(self, cups):
        self.cups_min = min(cups)
        self.cups_max = max(cups)
        self.cups_len = len(cups)

        self.cups = LinkedList()
        self.node_lookup = {}
        for cup in cups:
            node = Node(cup)
            if self.cups.head == None:
                self.cups.head = node
                prev_node = node
            else:
                prev_node.next = node
                prev_node = node

            self.node_lookup[str(cup)] = node

        # Make cyclic
        node.next = self.cups.head

        self.num_pick_up = 3

    def do_move(self):
        # Pick up the 3 cups after current cup
        # and remove them for the current linked list
        cups_to_move = []

        curr_node = self.cups.head
        for _ in range(3):
            curr_node = curr_node.next
            cups_to_move.append(curr_node)

        self.cups.head.next = curr_node.next

        # Get destination cup
        dest_cup_value = self.cups.head.data - 1
        if dest_cup_value < self.cups_min:
            dest_cup_value = self.cups_max

        dest_cup = self.node_lookup[str(dest_cup_value)]

        while dest_cup in cups_to_move:
            dest_cup_value -= 1
            if dest_cup_value < self.cups_min:
                dest_cup_value = self.cups_max

            dest_cup = self.node_lookup[str(dest_cup_value)]

        # Insert the cups after the destination cup
        insert_before_cup = dest_cup.next
        dest_cup.next = cups_to_move[0]
        cups_to_move[-1].next = insert_before_cup

        # increase index
        self.cups.rotate()

    def play(self, num_moves=100):
        for _ in range(num_moves):
            if (_ % 10000) == 0:
                print("done ", _)
            self.do_move()

    def get_cups_after_one(self):
        output = ""

        # Could use the node_lookups, but
        # thought it would be fun to write list traversing code :)
        one_cup = self.cups.find_node(1)

        node = one_cup.next
        while node != one_cup:
            output += str(node.data)

            node = node.next

        return output

    def get_prod_2_cups_after_1(self):
        one_cup = self.cups.find_node(1)

        output = 1

        node = one_cup.next
        for _ in range(2):
            output *= node.data

            node = node.next
        return output


def part1_solve(game):
    game.play(100)
    return game.get_cups_after_one()


def part2_solve(game):
    game.play(10000000)
    return game.get_prod_2_cups_after_1()


if __name__ == "__main__":

    # input = parse_input_p1(get_input(PATH + "real_input"))
    # print(part1_solve(input))

    # input = parse_input(get_input(PATH + "test_input"))
    # print(part2_solve(input))

    input = parse_input(get_input(PATH + "real_input"))
    print(part2_solve(input))
