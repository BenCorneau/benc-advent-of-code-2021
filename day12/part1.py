import util
from collections import defaultdict


def parse_input(s):
    return s.split("-")


def run():
    data = util.read_file("day12/input.txt", parse_input)
 
    nodes = defaultdict(list)
    for a,b in data:
        nodes[a].append(b)
        if b != "end":
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
        elif is_large_cave(next) or next not in path:
            paths.extend(visit(next_path, nodes))
    
    return paths

def is_large_cave(node):
    return node != node.lower()
