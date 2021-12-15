import util
from collections import defaultdict


def parse_input(data):
    template = data[0]
    
    rules = {}
    for row in data[1:]:
        pair,insert = row.split(" -> ")
        pair_a,pair_b = pair
        rules[pair]=[pair_a+insert, insert+pair_b]

    return template, rules
               

def run():
    data = util.read_file("day14/input.txt")
    template, rules = parse_input(data)
    return calc(template, rules)


def calc(template, rules):
    polymer = split_polymer(template)

    for i in range(40):
        polymer = step(polymer, rules)
       
    counts = element_count(polymer)

    min_count = min(counts.values())
    max_count = max(counts.values())
    return max_count - min_count


def split_polymer(polymer):
    parts = defaultdict(int)
    for i in range(1, len(polymer)):
        parts[polymer[i-1:i+1]] += 1
    
    return parts


def step(polymer, rules):

    new_polymer = defaultdict(int)
    for pair,count in polymer.items():
        a,b =rules[pair]
        new_polymer[a]+= count
        new_polymer[b]+= count
    
    return new_polymer
    

def element_count(polymer):
    counts = defaultdict(int)
    for pair, count in polymer.items():
        a,b = pair
        counts[a] += count
        counts[b] += count

    for k,v in counts.items():
        counts[k] = (v+1)//2
    return counts
    