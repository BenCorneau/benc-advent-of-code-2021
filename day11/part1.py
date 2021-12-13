import util


class Grid(object):

    @property
    def rows(self): return len(self.data)

    @property
    def cols(self): return len(self.data[0])

    def __init__(self, data):
        self.data = data

    def __getitem__(self, point):
        r,c = point
        return self.data[r][c]

    def __setitem__(self, point, value):
        r,c = point
        self.data[r][c] = value

    def points(self):
        for r in range(self.rows):
            for c in range(self.cols):
                yield (r,c)
    
    def print(self):
        for r in self.data:
            print("".join(map(str,r)))
    
    def valid_point(self, point):
        r,c = point
        if r<0 or c<0: return False
        if r >= self.rows: return False   
        if c >= self.cols: return False 
        return True


def parse_input(line):
    return [int(x) for x in line]


def run():
    data = util.read_file("day11/input.txt", parse_input)
    grid = Grid(data)
    return calc(grid)
    

def calc(grid):
    flash_count = 0
    for i in range(100):
        flash_count += step(grid)  
    return flash_count

    
def step(grid):
    for point in grid.points():
        grid[point] += 1
    
    more_flashes = True
    flash_count = 0
    while more_flashes:   
        more_flashes = False
        for point in grid.points():
            if grid[point] > 9:
                flash(grid, point)
                flash_count += 1
                more_flashes = True

    return flash_count
    

def flash(grid, point):
  
    grid[point] = 0

    def increase_point(point):
        if grid.valid_point(point) and 0 < grid[point] < 10:
            grid[point] += 1 

    #top-leftt, top-center, top-right
    increase_point(offset(point, -1, -1)) 
    increase_point(offset(point, -1,  0))
    increase_point(offset(point, -1,  1))

    #left & right
    increase_point(offset(point, 0, -1)) 
    increase_point(offset(point, 0,  1)) 

    #bottom-left, bottom-center, bottom-right
    increase_point(offset(point, 1, -1)) 
    increase_point(offset(point, 1,  0))
    increase_point(offset(point, 1,  1))


def offset(point, dr=0, dc=0):
    r,c = point
    return (r+dr, c+dc)