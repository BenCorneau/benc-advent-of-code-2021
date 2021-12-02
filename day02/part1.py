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
    for direction, distance in data:
        if direction == "up":
            depth -= distance
        
        if direction == "down":
            depth += distance
        
        if direction == "forward":
            horizontal_pos += distance
    
    return depth, horizontal_pos
            
