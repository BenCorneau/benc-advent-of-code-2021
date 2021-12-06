import util
from collections import defaultdict

def parse_input(s):
    def parse_point(point):
        x,y = point.split(",")
        return int(x), int(y)
    
    p1,p2 = s.split(" -> ")
    return parse_point(p1), parse_point(p2)


def run():
    input = util.read_file("day05/input.txt", parse_input)
    result = calc(input)
    print("result", result)


def calc(lines):
    points = defaultdict(lambda:0)
    
    for p1,p2 in lines:
        for point in calc_points(p1,p2):
            points[point] += 1

    return len([v for v in points.values() if v>= 2])

  
def _range(a,b):
    step=1 if a<b else -1 
    return range(a,b+step,step)


def calc_points(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    if x1 == x2:
        for y in _range(y1,y2):
            yield(x1,y)
    elif y1 == y2:
        for x in _range(x1, x2):
            yield(x,y1)
    else: # diagonal - exactly 45 degrees
        xs = _range(x1,x2)
        ys = _range(y1,y2)
        for point in zip(xs,ys):
            yield point
