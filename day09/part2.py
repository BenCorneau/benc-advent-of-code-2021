import util

def parse_input(s):
    return [int(ch) for ch in s]

def run():
    grid = util.read_file("day09/input.txt", parse_input)
    return calc(grid)


def calc(grid):
    basin_sizes = {pt:calculate_basin_size(grid, pt) for pt in find_low_points(grid)}
    biggest = sorted(basin_sizes.values())[-3:]
    return biggest[0] * biggest[1] * biggest[2]


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


def calculate_basin_size(grid, point):
    basin_points = set()
    recusive_basin_check(grid, point, basin_points)
    return len(basin_points)


def recusive_basin_check(grid, point, points):
    points.add(point)
    r,c = point
   
    up = (r-1,c)
    if r > 0 and up not in points and grid[r-1][c] != 9:
        recusive_basin_check(grid, up, points)
    
    left = (r,c-1)   
    if c > 0 and left not in points and grid[r][c-1] != 9:
        recusive_basin_check(grid, left, points)
    
    down = (r+1,c)
    if r < len(grid)-1 and down not in points and grid[r+1][c] != 9:
        recusive_basin_check(grid, down, points)
    
    right = (r,c+1)
    if c < len(grid[0])-1 and right not in points and grid[r][c+1] != 9:
        recusive_basin_check(grid, right, points)
