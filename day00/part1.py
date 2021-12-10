import util
from collections import defaultdict


def parse_input(s):
    return s


def run():
    data = util.read_file("dayXX/input_sample.txt", parse_input)
    data = util.read_line("dayXX/input_sample.txt", int)
    return calc(data)
    

def calc(data):
    return len(data)
