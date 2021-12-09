import util
from collections import defaultdict


def parse_input(s):
    a, b = s.split("|")
    wire_segments = a.split()
    output_segments = b.split()
    return wire_segments, output_segments


def run():
    data = util.read_file("day08/input.txt", parse_input)
    return calc(data)

# number | segments
#   0    |     6 
#   1    |     2 
#   2    |     5 
#   3    |     5 
#   4    |     4 
#   5    |     5 
#   6    |     6 
#   7    |     3 
#   8    |     7 
#   9    |     6 

#segments
#2 = [ 1 ]
#3 = [ 7 ]
#4 = [ 4 ]
#5 = [ 2 3 5 ]
#6 = [ 0 6 9 ]
#7 = [ 8 ]

def calc(data):
    count = 0
    for wire_segments, output_segments in data:
        for segments in output_segments:
            if len(segments) in (2,3,4,7):
                count += 1
    return count
