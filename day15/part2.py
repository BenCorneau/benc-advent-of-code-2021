import util
from util import Grid

from collections import defaultdict
import heapq


def run():
    data = util.read_file("day15/input.txt", lambda l:[int(x) for x in l])
    data = expand_data(data)

    grid = Grid(data)
    return calc(grid)


def expand_data(data):
    def n(v): return v%9+1

    def expand_row(row):
        next_row = row
        expanded_row = []
        expanded_row.extend(next_row)
        for i in range(4):
            next_row = [n(p) for p in next_row]
            expanded_row.extend(next_row)
        return expanded_row

    expanded_rows = []
    for row in data:
        expanded = expand_row(row)
        expanded_rows.append(expanded)

    #duplicate_rows
    original_rows = len(expanded_rows)
    for duplicate_index in range(4):
        for row_index in range(original_rows):
            src_index = duplicate_index * original_rows + row_index
            src_row = expanded_rows[src_index]
            new_row = [n(p) for p in src_row]
            expanded_rows.append(new_row)

    return expanded_rows


def calc(grid):

    start_pos = (0,0)
    end_pos = (grid.width-1, grid.height-1)
    shortest_path = find_shortest_path_astar(grid, start_pos, end_pos)
    #print_grid(grid, shortest_path)

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


class Heap:
    def __init__(self):
        self._data = []
        self._contains = set([])

    def add(self, item, cost):
        heapq.heappush(self._data, (cost, item))
        self._contains.add(item)

    def pop(self):
        cost, item = heapq.heappop(self._data)
        self._contains.remove(item)
        return item

    def __contains__(self, item):
        return item in self._contains

    def __len__(self):
        return len(self._contains)


class NodeInfo:
    def __init__(self, previous=None, cost_from_start=None, estimate_to_end=None):
        self.previous = previous
        self.cost_from_start = cost_from_start
        self.estimate_to_end = estimate_to_end


def find_shortest_path_astar(grid, start, destination):

    #heuristic function calculates best case cost to reach destination from p
    def heuristic(p):
        return (abs(p[0]-destination[0]) + abs(p[1]-destination[1]))

    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    open_set = Heap()
    open_set.add(item=start, cost=heuristic(start))

    tracked_nodes = defaultdict(lambda:NodeInfo())
    tracked_nodes[start] = NodeInfo(cost_from_start=0, estimate_to_end=heuristic(start))

    while open_set:
        current_node = open_set.pop()
        if current_node == destination:
            #build path from end to start
            shortest_path = []
            next = destination
            while next != start:
                shortest_path.append(next)
                next = tracked_nodes[next].previous

            shortest_path.reverse()
            return shortest_path

        node_info = tracked_nodes[current_node]
        for neighbor in grid.adjacent_points(current_node):
            neighbor_info = tracked_nodes[neighbor]

            cost_through_node = node_info.cost_from_start + grid[neighbor]
            if neighbor_info.cost_from_start is None or cost_through_node < neighbor_info.cost_from_start:

                # Found a better path
                neighbor_info.previous = current_node
                neighbor_info.cost_from_start = cost_through_node
                neighbor_info.estimate_to_end = cost_through_node + heuristic(neighbor)

                if neighbor not in open_set:
                    open_set.add(neighbor, cost=neighbor_info.estimate_to_end)
                
    # no path found
    return []