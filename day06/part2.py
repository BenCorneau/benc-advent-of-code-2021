import util

def run():
    input = util.read_line("day06/input.txt", int)
    result = calc(input)
    print("result", result)
 
      
DAYS = 256
def calc(input):
    fish_state = [0]*9
    
    for state in input:
        fish_state[state] += 1
    
    for d in range(0, DAYS):
        fish_state = calc_next_sate(fish_state)
         
    return sum(fish_state) 

def calc_next_sate(current_state):
    new_sate = current_state[1:] + current_state[0:1]
    new_sate[6] += current_state[0]
    return new_sate  
