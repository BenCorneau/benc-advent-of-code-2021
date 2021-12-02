import util


def run():
    input = util.read_file_int("day01/input.txt")
    
    result = count_increases(input)
    print("result", result)
    

def count_increases(data):
    increases = 0
    previous = data[0]
    for d in data:
        if d-previous > 0:
            increases+=1
        previous = d
    return increases
            
