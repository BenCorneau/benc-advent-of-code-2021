import util
from PIL import Image

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


WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)
GREEN = (  0,255,  0)

def calc(points, folds):

    max_x = max((x for x,y in points))
    max_y = max((y for x,y in points))
    img = Image.new( 'RGB', (max_x+1, max_y+1), WHITE) 
   

    #print the fold line
    for y in range(max_y):
         img.putpixel((655, y), BLUE)
   
    points = fold(points, folds[0])
    
    for x,y in points:
        if img.getpixel((x,y)) == WHITE:
            img.putpixel((x, y), RED)
        else:
            img.putpixel((x, y), BLACK)


    for x,y in points:
        img.putpixel((x, y), BLACK)
    img.save("layout_3.png", "PNG")

    print("points", len(points))
    return len(points)


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
