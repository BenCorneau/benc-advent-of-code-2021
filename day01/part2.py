import util


def run():
    input = util.read_file("day01/input.txt", int)
    
    result = count_increases_sliding_window(input)
    print("result", result)


WINDOW_SIZE = 3
def count_increases_sliding_window(data):

    increases = 0
    for i in range(WINDOW_SIZE, len(data)):
        if data[i] - data[i-WINDOW_SIZE] > 0:
            increases+=1
 
    return increases
            
