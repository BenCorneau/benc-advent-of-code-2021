import util
from collections import defaultdict

delimiters = [
    ('(',')'),
    ('[',']'),
    ('{','}'),
    ('<','>')
]
open_delimiters = set([o for o,c in delimiters])
delimiter_pair_by_closer = {c:o for o,c in delimiters}

ERROR_SCORE = {
    ')' :     3,
    ']' :    57,
    '}' :  1197,
    '>' : 25137
}

def run():
    data = util.read_file("day10/input.txt", str)
    return calc(data)
    
def calc(data):
    score = 0
    for line in data:
        bad_char = find_first_illegal_char(line)
        if bad_char:
            score += ERROR_SCORE[bad_char]

    return score

def find_first_illegal_char(line):
    delimiter_stack = []
    for c in line:
        if c in open_delimiters:
            delimiter_stack.append(c)
        else:
            if not delimiter_stack:
                return c
            
            if delimiter_pair_by_closer[c] != delimiter_stack.pop():
                return c
    
    return None
