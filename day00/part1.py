import util
from collections import defaultdict


def parse_input(s):
    return s


def run():
    input = util.read_file("dayXX/input_sample.txt", parse_input)
    input = util.read_line("dayXX/input_sample.txt", int)
    result = calc(input)
    print("result", result)


def calc(input):
    return len(input)
