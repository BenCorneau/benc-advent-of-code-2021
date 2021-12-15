import util
from collections import defaultdict


def parse_input(data):
    template = data[0]
    
    rules = {}
    for row in data[1:]:
        a,b = row.split(" -> ")
        rules[a]=b
     
    return template, rules
               

def run():
    data = util.read_file("day14/input.txt")
    template, rules = parse_input(data)
    return calc(template, rules)


def calc(template, rules):

    polymer = template
    for i in range(10):
        polymer = "".join(step(polymer, rules))
     
    element_count = defaultdict(int)
    for e in polymer:
        element_count[e] += 1

    min_count = min(element_count.values())
    max_count = max(element_count.values())
    return max_count - min_count


def step(polymer, rules):

    for i in range(len(polymer)-1):
        yield polymer[i]
        match = rules.get(polymer[i:i+2])
        if match:
            yield match
    
    yield polymer[-1]
