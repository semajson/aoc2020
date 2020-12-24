import re
import sys
from dataclasses import dataclass
import math
import copy

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day22/"

# Part 1


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


class Game:
    def __init__(self, player1_deck, player2_deck):
        self.player1_deck = player1_deck
        self.player2_deck = player2_deck
        # self.turn = "player_1"

    def play(self):
        while (self.player1_deck != []) and (self.player2_deck != []):
            player1_card = self.player1_deck.pop(0)
            player2_card = self.player2_deck.pop(0)

            if player1_card > player2_card:
                self.player1_deck.append(player1_card)
                self.player1_deck.append(player2_card)
            elif player2_card > player1_card:
                self.player2_deck.append(player2_card)
                self.player2_deck.append(player1_card)
            else:
                raise Exception

    def get_win_score(self):
        if len(self.player1_deck) == 0:
            winner_deck = self.player2_deck
        elif len(self.player2_deck) == 0:
            winner_deck = self.player1_deck
        else:
            raise Exception

        score = 0
        for i in range(len(winner_deck)):
            score += winner_deck[i] * (len(winner_deck) - i)

        return score


def parse_input(input):
    player1_deck = []
    player2_deck = []

    current_deck = player1_deck
    for line in input:
        if line.startswith("Player 1") or (line == ""):
            pass
        elif line.startswith("Player 2"):
            current_deck = player2_deck
        else:
            current_deck.append(int(line))

    return Game(player1_deck=player1_deck, player2_deck=player2_deck)


def part1_solve(game):
    game.play()
    print("here")
    return game.get_win_score()


if __name__ == "__main__":
    input = parse_input(get_input(PATH + "test_input"))
    print(part1_solve(input))

    input = parse_input(get_input(PATH + "real_input"))
    print(part1_solve(input))
