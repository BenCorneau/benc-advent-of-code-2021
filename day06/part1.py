import util

def run():
    input = util.read_line("day06/input.txt", int)
    result = calc(input)
    print("result", result)
    

def calc_lanternfish_for_days(start_number, days):
    fish = [start_number]
    
    for d in range(0, days):
        
        for i in range(0, len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1

    return len(fish)    


DAYS = 80
def calc(input):
    fish_lookup = {}

    for i in range(0,9):
        fish_lookup[i] = calc_lanternfish_for_days(i,DAYS)
    
    total_fish = 0
    for f in input:
        total_fish += fish_lookup[f]

    return total_fish
