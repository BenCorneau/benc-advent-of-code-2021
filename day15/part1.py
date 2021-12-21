import util
from util import Grid


def run():
    data = util.read_file("day15/input.txt", lambda l:[int(x) for x in l])
    grid = Grid(data)
    return calc(grid)


def calc(grid):
  
    start_pos = (0,0)
    end_pos = (grid.width-1, grid.height-1)
    shortest_path = find_shortest_path_dijkstras(grid, start_pos, end_pos)

    print_grid(grid, shortest_path)

    cost = sum([grid[p] for p in shortest_path] )
    return cost


def print_grid(grid, path):

    for y in range(grid.height):
        row = ""
        for x in range(grid.width):
            if (x,y) in path:
                row += "█"
            else:
                row += str(grid[(x,y)])
        print(row)


def find_shortest_path_dijkstras(grid, start, destination):
         
    tracked_path = {}
    visited = {start : 0}
    nodes = set(grid.points())

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
       
        for next_point in grid.adjacent_points(min_node):
            distance = visited[min_node] + grid[next_point]
            if next_point not in visited or distance < visited[next_point]:
                visited[next_point] = distance
                tracked_path[next_point] = min_node
    
    
    #build path from end to start
    shortest_path = []
    next = destination
    while next != start:
        shortest_path.append(next)
        next = tracked_path[next]

    shortest_path.reverse()
    return shortest_path