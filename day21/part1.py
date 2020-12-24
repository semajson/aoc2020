import re
import sys
from dataclasses import dataclass
import math
import copy

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day21/"

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


class Allergen:
    def __init__(self, name):
        self.name = name
        self.pos_ingredients = None

    def update_pos_ingredients(self, ingredients):
        ingredients = set(ingredients)

        if self.pos_ingredients == None:
            self.pos_ingredients = ingredients
        else:
            # Here, the new possible ingredients should be
            # the intersetion of the two sets:
            self.pos_ingredients = self.pos_ingredients.intersection(ingredients)

    def __repr__(self):
        return self.name


@dataclass
class Food:
    ingredients: list
    allergens: list


def parse_input(input):
    foods = []
    found_allergens = {}

    for food in input:
        food = food.replace("(", "").replace(")", "").replace(",", "")
        food = food.split(" contains ")
        ingredients = food[0].split(" ")
        allergens_str = food[1].split(" ")

        # js9 note, is hungarian notation bad here?
        allergens = []
        for allergen_str in allergens_str:
            if allergen_str not in found_allergens:
                allergen = Allergen(allergen_str)
                found_allergens[allergen_str] = allergen
            else:
                allergen = found_allergens[allergen_str]

            allergens.append(allergen)

        foods.append(Food(ingredients, allergens))
    return foods


def part1_solve(foods):
    all_ingredients = []
    all_allergens = set()
    for food in foods:
        all_ingredients.extend(food.ingredients)
        all_allergens.update(set(food.allergens))

        for allergen in food.allergens:
            allergen.update_pos_ingredients(food.ingredients)

    # Actually answer part 1
    count = 0
    for ingredient in all_ingredients:
        has_allergen = False
        for allergen in all_allergens:
            if ingredient in allergen.pos_ingredients:
                has_allergen = True
                break
        if not has_allergen:
            count += 1

    return count


if __name__ == "__main__":
    input = parse_input(get_input(PATH + "test_input"))
    print(part1_solve(input))

    input = parse_input(get_input(PATH + "real_input"))
    print(part1_solve(input))
