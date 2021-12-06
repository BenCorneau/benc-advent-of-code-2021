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

    for x in range(0,10):
        row = []
        for y in range(0,10):
            row.append(points[(x,y)])
        print(row)
        
    
    return len([v for v in points.values() if v>= 2])

  
def calc_points(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    if x1 == x2:
        min_y = min(y1,y2)
        max_y = max(y1,y2)
        for y in range(min_y,max_y+1):
            yield(x1,y)
    elif y1 == y2:
        min_x = min(x1,x2)
        max_x = max(x1,x2)
        for x in range(min_x,max_x+1):
            yield(x,y1)