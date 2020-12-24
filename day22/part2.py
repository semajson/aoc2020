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
        self.previous_rounds = []
        self.winner = None

    def play(self):
        while (self.player1_deck != []) and (self.player2_deck != []):
            # If this is a repeat of previous round, player 1 wins
            if [self.player1_deck, self.player2_deck] in self.previous_rounds:
                self.winner = "player1"
                break

            self.previous_rounds.append(
                [self.player1_deck.copy(), self.player2_deck.copy()]
            )

            player1_card = self.player1_deck.pop(0)
            player2_card = self.player2_deck.pop(0)

            # Get winner
            if (player1_card <= len(self.player1_deck)) and (
                player2_card <= len(self.player2_deck)
            ):
                # Decide winner with sub game
                sub_player1_deck = self.player1_deck[:player1_card]
                sub_player2_deck = self.player2_deck[:player2_card]
                sub_game = Game(
                    player1_deck=sub_player1_deck, player2_deck=sub_player2_deck
                )
                sub_game.play()

                round_winner = sub_game.winner
                assert round_winner != None

            else:
                # Decide winner with normal rules
                if player1_card > player2_card:
                    round_winner = "player1"
                elif player2_card > player1_card:
                    round_winner = "player2"

            # Add cards to the bottom of the deck
            if round_winner == "player1":
                self.player1_deck.append(player1_card)
                self.player1_deck.append(player2_card)
            elif round_winner == "player2":
                self.player2_deck.append(player2_card)
                self.player2_deck.append(player1_card)
            else:
                raise Exception

        if len(self.player1_deck) == 0:
            self.winner = "player2"
        elif len(self.player2_deck) == 0:
            self.winner = "player1"

    def get_win_score(self):
        if self.winner == "player1":
            winner_deck = self.player1_deck
        elif self.winner == "player2":
            winner_deck = self.player2_deck
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


def part2_solve(game):
    game.play()
    print("here")
    return game.get_win_score()


if __name__ == "__main__":
    input = parse_input(get_input(PATH + "test_input"))
    print(part2_solve(input))

    input = parse_input(get_input(PATH + "test_input_1"))
    print(part2_solve(input))

    input = parse_input(get_input(PATH + "real_input"))
    print(part2_solve(input))
