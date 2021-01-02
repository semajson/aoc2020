import re
import sys
from dataclasses import dataclass
import math
import copy

sys.path.append("c:\\Users\\james_pc\\projects\\aoc2020\\")
sys.path.append("./..")

from utils import time_algo

PATH = "day18/"

# trying to use pratt parsing
# found on https://eli.thegreenplace.net/2010/01/02/top-down-operator-precedence-parsing
# https://web.archive.org/web/20200505140845/http://effbot.org/zone/simple-top-down-parsing.htm


# lbp = left binding power
# rbp = right binding power
# binding powers control in what order opterations are preformed
# nud = function,  null denotation, e.g. whe have "- 4 + 5", "-" isn't acting on previous number, so call nud method
# led =  function (left denotation). e.g., in above we would call led for "+" operator to act on 4


def get_input(filename):
    my_file = open(filename, "r")
    content = my_file.readlines()
    return [line.rstrip() for line in content]


# This is a generator (as it has yields)
# It means we don't have to load the entire expression into memory at once.
# Might be overkill here, but it's cool
def tokenize(statement):
    statement = list(statement)
    for char in statement:
        if char == "+":
            yield operator_add_token()
        elif char == "-":
            yield operator_sub_token()
        elif char == "*":
            yield operator_mul_token()
        elif char == "/":
            yield operator_div_token()
        elif char == "^":
            yield operator_pow_token()
        elif char == "(":
            yield operator_lparen_token()
        elif char == ")":
            yield operator_rparen_token()
        elif char.isdigit():
            yield literal_token(char)
        else:
            raise SyntaxError("unknown operator: %s", char)
    yield end_token()


def match(tok=None):
    global token
    if tok and tok != type(token):
        raise SyntaxError("Expected %s" % tok)
    token = next()


def parse(statement):
    global token, next
    next = tokenize(statement).__next__

    # get the first token
    token = next()
    return expression()


def expression(rbp=0):
    global token
    t = token
    token = next()
    left = t.nud()
    while rbp < token.lbp:
        t = token
        token = next()
        left = t.led(left)
    return left


class literal_token(object):
    def __init__(self, value):
        self.value = int(value)

    def nud(self):
        return self.value


class operator_add_token(object):
    # I suspect here that lbp is a property of the class,
    # not of the object here (like a static)
    lbp = 20

    def nud(self):
        return expression(100)

    def led(self, left):
        right = expression(operator_add_token.lbp)
        return left + right


class operator_sub_token(object):
    lbp = 20

    def nud(self):
        return -expression(100)

    def led(self, left):
        return left - expression(operator_sub_token.lbp)


class operator_mul_token(object):
    lbp = 10

    def led(self, left):
        return left * expression(operator_mul_token.lbp)


class operator_div_token(object):
    lbp = 20

    def led(self, left):
        return left / expression(operator_div_token.lbp)


class operator_pow_token(object):
    lbp = 30

    def led(self, left):
        return left ** expression(operator_pow_token - 1)


class operator_lparen_token(object):
    lbp = 0

    def nud(self):
        # I modified called here to explicity call
        # expression with lbp of right parenthathese
        # so we will keep going through expression until find other closing bracket, then
        # return the value
        expr = expression(operator_rparen_token.lbp)

        # from expression, we have iterated through the statement so actually just before the ")",
        # call match to move the token along one
        # I don't like this really, as it is expr() not match finding the ")" token...
        match(operator_rparen_token)
        return expr


class operator_rparen_token(object):
    lbp = 0


class end_token(object):
    lbp = 0


def part2_solve(statements):
    sum = 0
    for statement in statements:
        statement = statement.replace(" ", "")
        sum += parse(statement)
    return sum


if __name__ == "__main__":
    input = get_input(PATH + "test_input_1")
    print(part2_solve(input))

    input = get_input(PATH + "real_input")
    print(part2_solve(input))
