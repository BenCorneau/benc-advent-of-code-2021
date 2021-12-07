import util

def run():
    data = util.read_line("day07/input.txt", int)
    result = calc(data)
    print("result", result)


def calc(data):   
    middle_position = median(data)
    return calculate_fuel_cost(data, middle_position)


def calculate_fuel_cost(crab_positions, target_position):
    return sum((abs(p-target_position) for p in crab_positions))


def median(data):
    sorted_data = sorted(data)
    mid = len(sorted_data)//2
    return sorted_data[mid]    
