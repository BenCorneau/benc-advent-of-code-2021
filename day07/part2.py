import util


def run():
    data = util.read_line("day07/input.txt", int)
    result = calc(data)
    print("result", result)


def calc(data):
    def all_fuel_costs():
        for pos in range(min(data), max(data)):
            yield calculate_fuel_cost(data, pos)
      
    return min(all_fuel_costs())


def calculate_fuel_cost(crab_positions, target_position):
    return sum((distance_cost(abs(p-target_position)) for p in crab_positions))


#pos cost | doubled | 
#1  =  1  |    2    | 1*2 
#2  =  3  |    6    | 2*3 
#3  =  6  |   12    | 3*4
#4  = 10  |   20    | 4*5
#5  = 15  |   30    | 5*6
def distance_cost(d):
    return (d*(d+1))//2