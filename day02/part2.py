import util


def parse_input(command):
    direction, distance = command.split(" ")
    return direction, int(distance)


def run():
    input = util.read_file("day02/input.txt", parse_input)
    depth, horizontal_pos = calculate_movement(input)
    print("result", depth, horizontal_pos)
    print(depth * horizontal_pos)
 
    
def calculate_movement(data):
    depth = 0
    horizontal_pos = 0
    aim = 0
    for dir, distance in data:
        if dir == "up":
            aim -= distance
        
        if dir == "down":
            aim += distance
        
        if dir == "forward":
            horizontal_pos += distance
            depth += aim * distance
    return depth, horizontal_pos
            