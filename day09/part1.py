import util

def parse_input(s):
    return [int(ch) for ch in s]

def run():
    grid = util.read_file("day09/input.txt", parse_input)
    return calc(grid)


def calc(grid):
    return sum( ( grid[r][c]+1 for r,c in find_low_points(grid) ) )
   
   
def find_low_points(grid):
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if is_low_point(grid, (r,c)):
                yield (r,c)


def is_low_point(grid, point):
    r,c = point
    value = grid[r][c]

    if r > 0 and value >= grid[r-1][c]:
        return False

    if c > 0 and value >= grid[r][c-1]:
        return False
    
    if r < len(grid)-1 and value >= grid[r+1][c]:
        return False
    
    if c < len(grid[0])-1 and value >= grid[r][c+1]:
        return False

    return True
