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


def part2_solve(foods):
    all_allergens = set()
    for food in foods:
        all_allergens.update(set(food.allergens))

        for allergen in food.allergens:
            allergen.update_pos_ingredients(food.ingredients)

    # Ingredients hac only have 1 allergen,
    # and only ingredient for each allergen
    # So sudoku this to match allergens to ingredients
    done_pass = True
    while done_pass:
        done_pass = False

        for allergen in all_allergens:
            if len(allergen.pos_ingredients) == 1:
                ingredient = next(iter(allergen.pos_ingredients))

                for allergen_r in all_allergens:
                    if allergen == allergen_r:
                        continue
                    if ingredient in allergen_r.pos_ingredients:
                        done_pass = True
                        allergen_r.pos_ingredients.remove(ingredient)

    # Now solve the puzzle
    allergic_ingredients = []
    all_allergens = list(all_allergens)

    # how does this lambda work?
    all_allergens.sort(key=lambda x: x.name)

    for allergen in all_allergens:
        allergic_ingredients.append(next(iter(allergen.pos_ingredients)))

    return ",".join(allergic_ingredients)


if __name__ == "__main__":
    input = parse_input(get_input(PATH + "test_input"))
    print(part2_solve(input))

    input = parse_input(get_input(PATH + "real_input"))
    print(part2_solve(input))
