import util


def run():
    input = util.read_file("day03/input.txt", str)
    oxygen_rating  = calculate_oxygen_rating(input)
    co2_rating  = calculate_co2_rating(input)
    print("result", oxygen_rating, co2_rating)
    print(oxygen_rating * co2_rating)


def calculate_co2_rating(data):
    return filter_value_by_bit(data, least_common_value)
  

def calculate_oxygen_rating(data):
    return filter_value_by_bit(data, most_common_value)
  

def filter_value_by_bit(data, bit_criteria_filter_func):
    bits = len(data[0])
     
    for bit in range(0, bits):
        required_bit = bit_criteria_filter_func(data, bit)
        data = [v for v in data if v[bit] == required_bit]
        if len(data) == 1:
            value = data[0]
            return int(value, 2)


def most_common_value(data, bit_position):
    count = 0
    for v in data:
        if v[bit_position] == '1':
            count += 1

    if count < len(data)/2:
        return '0'
    return '1'


def least_common_value(data, bit_position):
    if most_common_value(data, bit_position) == '0':
        return '1'
    else:
        return '0'
