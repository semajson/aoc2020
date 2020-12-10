import re
import sys

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day7/"

# Part 1
def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


class ChildNodeLink:
    def __init__(self, bag, number):
        self.bag = bag
        self.number = number


class TreeNode:
    def __init__(self, bag_colour):
        self.bag_colour = bag_colour
        self.parent_bags = []
        self.child_bags = []

    def find_node(self, bag_colour):
        if self.bag_colour == bag_colour:
            return self

        for parent in self.parent_bags:
            found_bag = parent.find_node(bag_colour)
            if found_bag != None:
                return found_bag

        # Haven't found the node, return None
        return None

    def add_children(self, bag_colour, child_bag_dicts, node_dict):
        # Convert the bag colours to bag link objects
        child_bags = []
        for child_bag_dict in child_bag_dicts:
            child_bags.append(
                ChildNodeLink(
                    bag=node_dict[child_bag_dict["colour"]],
                    number=int(child_bag_dict["number"]),
                )
            )

        if child_bags == []:
            child_bags = [ChildNodeLink(bag=node_dict["root"], number=0)]

        for child_bag in child_bags:
            self.child_bags.append(child_bag)
            child_bag.bag.parent_bags.append(self)

    def find_ancestors(self):
        # Use sets to prevent double counting
        ancestors = set(self.parent_bags)
        for parent in self.parent_bags:
            ancestors = ancestors | parent.find_ancestors()

        return ancestors

    def calc_total_num_bags(self):
        total_num_bags = 1
        for child_bag in self.child_bags:
            total_num_bags += child_bag.number * child_bag.bag.calc_total_num_bags()

        return total_num_bags

    def calc_total_num_child_bags(self):
        # -1 as to not include this bag
        return self.calc_total_num_bags() - 1


def parse_line(line):
    # Remvoe unnecessary words
    line = line.replace("bags", "")
    line = line.replace("bag", "")
    line = line.replace(".", "")

    # Split into the colours
    line = re.split("contain|,", line)
    line = [item.strip() for item in line]

    # Find bag colour
    bag_colour = line.pop(0)

    # Find sub_bags
    child_bag_dicts = []
    for child_bag in line:
        if child_bag == "no other":
            break

        child_bag = child_bag.split(" ")
        child_bag_colour = child_bag[1] + " " + child_bag[2]
        child_bag_number = child_bag[0]

        child_bag_dicts.append({"colour": child_bag_colour, "number": child_bag_number})

    return bag_colour, child_bag_dicts


def parse_input(input):
    root_node = TreeNode(bag_colour="root")

    # Make all the nodes in the tree first (without relationships)
    # We can't create the relationships here as well as the input file isn't ordered
    node_dict = {"root": root_node}
    for line in input:
        bag_colour, child_bag_dicts = parse_line(line)

        node_dict[bag_colour] = TreeNode(bag_colour)

    # Now build all the relationships between the nodes
    for line in input:
        bag_colour, child_bag_dicts = parse_line(line)

        node_dict[bag_colour].add_children(
            bag_colour=bag_colour,
            child_bag_dicts=child_bag_dicts,
            node_dict=node_dict,
        )

    return root_node


def part1_solve(tree):
    # Find the number of parents for the gold bag.
    gold_bag = tree.find_node("shiny gold")
    return len(gold_bag.find_ancestors())


def part2_solve(tree):
    # Find the number of bags within the gold bag

    gold_bag = tree.find_node("shiny gold")

    return gold_bag.calc_total_num_child_bags()


if __name__ == "__main__":

    # print(get_input("test_input"))

    test_input = parse_input(get_input(PATH + "test_input"))
    print(part1_solve(test_input))

    real_input = parse_input(get_input(PATH + "real_input"))
    print(part1_solve(real_input))

    test_input = parse_input(get_input(PATH + "test_input"))
    print(part2_solve(test_input))

    real_input = parse_input(get_input(PATH + "real_input"))
    print(part2_solve(real_input))

    # real_input = parse_input(get_input("real_input"))
    # print(part1_solve(real_input))
