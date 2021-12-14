import util

def parse_input(data):
    points = []
    folds = []
    for row in data:
        if row.startswith("fold along"):
            direction, position = row.replace("fold along ", "").split("=")
            folds.append((direction, int(position)))
        else:
            x,y = [int(v) for v in row.split(",")]
            points.append((x,y))

    return set(points), folds
               

def run():
    data = util.read_file("day13/input.txt")
    points, folds = parse_input(data)
    return calc(points, folds)


def fold(points, fold_info):

    def _fold_point(n, limit):
        if n  > limit:
            return limit-(n-limit)
        else:
            return n

    fold_dir, fold_pos = fold_info

    if fold_dir == 'x':
        return set([(_fold_point(x, fold_pos), y) for x,y in points])
    else:
        return set([(x, _fold_point(y, fold_pos)) for x,y in points])


def print_points(points):
    max_x = max((x for x,y in points))
    max_y = max((y for x,y in points))
    
    for y in range(max_y+1):
        row = ""
        for x in range(max_x+1):
            row += "█" if (x,y) in points else " "
        print(row)
            
def calc(points, folds):  

    for fold_info in folds:
        points = fold(points, fold_info)
    
    print_points(points)
