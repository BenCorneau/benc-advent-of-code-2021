import util


def run():
    input = util.read_file("day03/input.txt", str)
    gamma, epsilon  = calculate_power_consumption(input)
    print("result", gamma, epsilon)
    print(gamma * epsilon)
    
#
#result 1776 2319
#4118544

def calculate_power_consumption(data):
    
    bits = len(data[0])
    
    #list initilized to 0 with lengh equal to the number of bits in the first entry
    bit_counts = [0]*bits 
    
    for v in data:
        for bit in range(0, bits):
            if v[bit] == "1":
                bit_counts[bit] += 1

    gamma = 0
    for bit in range(0, bits):
        gamma <<= 1
        if bit_counts[bit] > len(data)/2:
            gamma |= 1
    
    #flip gamma bits
    epsilon = gamma ^ pow(2,bits)-1

    return gamma, epsilon

def calculate_power_consumption_as_strings(data):
    
    bits = len(data[0])
    
    #list initilized to 0 with lengh equal to the number of bits in the first entry
    bit_counts = [0]*bits 
    
    for v in data:
        for bit in range(0, bits):
            if v[bit] == "1":
                bit_counts[bit] += 1

    gamma = ""
    epsilon = ""
    for bit in range(0, bits):
        if bit_counts[bit] > len(data)/2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"


    return int(gamma,2), int(epsilon,2)
        
        
            
