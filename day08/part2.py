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
    

def calc(data):
    total = 0
    for wire_segments, output_segments in data:
        segments_to_number = calculate_number_segments(wire_segments)
        
        display_number = ""
        for output in output_segments: 
            display_number += str(segments_to_number[frozenset(output)])
        total += int(display_number)        
    return total


# numbers by segment count
#---------------
# 2 = [ 1 ]
# 3 = [ 7 ]
# 4 = [ 4 ]
# 5 = [ 2 3 5 ]
# 6 = [ 0 6 9 ]
# 7 = [ 8 ]

# segment layout
#---------------
#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

def calculate_number_segments(wire_number_segments):

    cluster_by_length = defaultdict(list)
    for w in wire_number_segments: cluster_by_length[len(w)].append(frozenset(w))
   
    number_segments = {}
    number_segments[1] = cluster_by_length[2][0]
    number_segments[7] = cluster_by_length[3][0]
    number_segments[4] = cluster_by_length[4][0]
    number_segments[8] = cluster_by_length[7][0]

    segments_cf = number_segments[1]
    segments_bd = number_segments[4] - segments_cf
    
    #2,3 or 5
    for cluster in cluster_by_length[5]:
        if segments_cf <= cluster:
            number_segments[3] = cluster
        elif segments_bd <= cluster:
            number_segments[5] = cluster
        else:
            number_segments[2] = cluster

    #0,6 or 9
    for cluster in cluster_by_length[6]:
        if not segments_bd <= cluster:
            number_segments[0] = cluster
        elif segments_cf <= cluster:
            number_segments[9] = cluster
        else:
            number_segments[6] = cluster
      
    #swap keys and values
    return {seg: num for num, seg in number_segments.items()}
