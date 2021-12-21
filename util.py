
  
def read_file(file, transform=str):
    with open(file, encoding="utf8") as f:
        return [transform(l.strip()) for l in f.readlines() if l.strip()]


def read_line(file, transform=str):
    with open(file, encoding="utf8") as f:
        line = f.readline()
        return [transform(v.strip()) for v in line.split(",") if v.strip()]


class Grid(object):

    @property
    def height(self): return len(self.data)

    @property
    def width(self): return len(self.data[0])

    def __init__(self, data):
        self.data = data

    def __getitem__(self, point):
        x,y = point
        return self.data[y][x]

    def __setitem__(self, point, value):
        x,y = point
        self.data[y][x] = value

    def points(self):
        for x in range(self.width):
            for y in range(self.height):
                yield (x,y)

    def print(self):
        for r in self.data:
            print("".join(map(str,r)))

    def valid_point(self, point):
        x,y = point
        if x<0 or y<0: return False
        if x >= self.width: return False
        if y >= self.height: return False
        return True

    def adjacent_points(self, point):
        x,y = point
        neighboors = [
            (x, y-1),
            (x, y+1),
            (x-1,y),
            (x+1,y)]

        return set([p for p in neighboors if self.valid_point(p)])
