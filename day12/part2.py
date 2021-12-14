import util
from collections import defaultdict


def parse_input(s):
    return s.split("-")


def run():
    data = util.read_file("day12/input.txt", parse_input)
 
    nodes = defaultdict(list)
    for a,b in data:
        nodes[a].append(b)
        if b != "end" and a != 'start':
            nodes[b].append(a)

    return calc(nodes)


def calc(nodes):
    paths = visit(['start'], nodes)
    return len(paths)

    
def visit(path, nodes):
    paths = []
    for next in nodes[path[-1]]:
        next_path = path + [next]
        if next == "end":
            paths.append(next_path)
        elif is_large_cave(next) or next not in path or at_most_two_visits_to_single_small_cave(next_path):
            paths.extend(visit(next_path, nodes))
    
    return paths


def is_large_cave(node):
    return node != node.lower()


def at_most_two_visits_to_single_small_cave(path):
    cave_count = defaultdict(int)
    for cave in path:
        if not is_large_cave(cave):
            cave_count[cave] += 1
    
    double_cave = False
    for cave,count in cave_count.items():
        if count > 2:return False
        if count == 2:
            if not double_cave:
                double_cave = True
            else:
                return False
    return True  
