import re
import sys

sys.path.append("./..")
from utils import time_algo

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


class TreeNode:
    def __init__(self, bag_colour):
        self.bag_colour = bag_colour
        self.parent_bags = []
        self.child_bags = []

    # Turn out can't use this method :{
    def find_node(self, bag_colour):
        if self.bag_colour == bag_colour:
            return self

        for parent in self.parent_bags:
            found_bag = parent.find_node(bag_colour)
            if found_bag != None:
                return found_bag

        # Haven't found the node, return None
        return None

    def add_children(self, bag_colour, child_bag_colours, node_dict):
        assert self.bag_colour == "root"

        node = node_dict[bag_colour]

        print("Adding node,", bag_colour)
        print("with child nodes ", child_bag_colours)

        # Convert the bag colours to bag objects
        child_bags = []
        for child_bag_colour in child_bag_colours:
            child_bags.append(node_dict[child_bag_colour])

        if child_bags == []:
            child_bags = [self.find_node("root")]

        for child_bag in child_bags:
            node.child_bags.append(child_bag)
            child_bag.parent_bags.append(node)

    def find_ancestors(self):
        # Use sets to prevent double counting
        ancestors = set(self.parent_bags)
        for parent in self.parent_bags:
            ancestors = ancestors | parent.find_ancestors()

        return ancestors


def parse_input(input):
    input.reverse()

    tree = TreeNode(bag_colour="root")

    # Make the nodes first
    node_dict = {}
    for rule in input:
        # Remvoe unnecessary words
        rule = rule.replace("bags", "")
        rule = rule.replace("bag", "")
        rule = rule.replace(".", "")

        # Split into the colours
        rule = re.split("contain|,", rule)
        rule = [item.strip() for item in rule]

        # Find bag colour
        bag_colour = rule.pop(0)

        node_dict[bag_colour] = TreeNode(bag_colour)

    # Now build all the relationships between the nodes
    for rule in input:
        # Remvoe unnecessary words
        rule = rule.replace("bags", "")
        rule = rule.replace("bag", "")
        rule = rule.replace(".", "")

        # Split into the colours
        rule = re.split("contain|,", rule)
        rule = [item.strip() for item in rule]

        # Find bag colour
        bag_colour = rule.pop(0)

        # Find sub_bags
        child_bag_colours = []
        for child_bag in rule:
            if child_bag == "no other":
                break

            child_bag = child_bag.split(" ")
            child_bag_colour = child_bag[1] + " " + child_bag[2]
            child_bag_number = child_bag[0]
            """
            contains_bags.append(
                {"number": child_bag[0], "bag": (child_bag[1] + " " + child_bag[2])}
            )
            """
            child_bag_colours.append(child_bag_colour)

        # Add this info to the tree
        tree.add_children(
            bag_colour=bag_colour,
            child_bag_colours=child_bag_colours,
            node_dict=node_dict,
        )

    return tree


def part1_solve(tree):
    # Find the number of parents for the gold bag.

    gold_bag = tree.find_node("shiny gold")
    return len(gold_bag.find_ancestors())


if __name__ == "__main__":

    # print(get_input("test_input"))

    test_input = parse_input(get_input("test_input"))
    print(part1_solve(test_input))

    real_input = parse_input(get_input("real_input"))
    print(part1_solve(real_input))
