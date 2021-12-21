import util
from collections import namedtuple


class BitStream:

    @property
    def pos(self): return self._pos

    def __init__(self, bits):
        self._bits = bits
        self._pos = 0

    def read_bits(self, length):
        remaining_bits = len(self._bits) - self._pos 
        assert length <= remaining_bits, f"length cannot exceed remaing bits in the packet. length={length}, remaining_bits={remaining_bits}"
        
        s = self._pos
        e = self._pos + length
        self._pos = e
        data = self._bits[s:e]
        #print(f"bits[{s}:{e}] = {data}")
        return data

    def read_int(self, length):
        return int(self.read_bits(length), 2)

Packet = namedtuple('Packet', ['version', 'type', 'value'])

def parse_data(data):
    def hex_to_bits(x):
        return  bin(int(x, 16)).replace("0b","").rjust(4,'0')
    return "".join((hex_to_bits(x) for x in data))

def run():
    data = util.read_line("day16/input.txt")[0]
    bits = parse_data(data)
    bit_stream = BitStream(bits)
    return calc(bit_stream)

        
def calc(bit_stream):
    packet = parse_packet(bit_stream)
    print_packet(packet)
    return compute_packet(packet)
    
def parse_packet(bit_stream):
   
    version = bit_stream.read_int(3)
    type_id = bit_stream.read_int(3)

    if type_id == 4:
        value = parse_literal(bit_stream)
        return Packet(version, type_id, value)
    else:
        return parse_operator(version, type_id, bit_stream)

def parse_literal(bit_stream):
    
    bits = ""
    more = True
    while more:
        more = bit_stream.read_int(1)
        bits += bit_stream.read_bits(4)
    return int(bits, 2)

def parse_operator(version, type_id, bit_stream):

    sub_packets = []
    length_type = bit_stream.read_int(1)
    if length_type == 0:
        sub_packet_length = bit_stream.read_int(15)
        end_pos = bit_stream.pos + sub_packet_length
        
        while bit_stream.pos < end_pos:
            sub_packets.append(parse_packet(bit_stream))
    else:
        sub_packet_count = bit_stream.read_int(11)
        for i in range(sub_packet_count):
            sub_packets.append(parse_packet(bit_stream))

    return Packet(version, type_id, sub_packets)


def print_packet(packet, level=0):
    if packet.type == 4:
        print(f"{'    '*level}type:LITERAL version:{packet.version} value:{packet.value}")
    else:
        print(f"{'    '*level}type:OP_{packet.type} version:{packet.version}")
        for p in packet.value:
            print_packet(p,level+1)
 

# 0 - sum
# 1 - multiply
# 2 - minimum
# 3 - maximum
# 4 - value
# 5 - greater than | a > b 
# 6 - less than | a > b
# 7 - equal | a==b
def compute_packet(packet):

    if packet.type == 4:
        return packet.value
    
    values = [compute_packet(p) for p in packet.value]

    if packet.type == 0: return sum(values)
    if packet.type == 1: return product(values)
    if packet.type == 2: return min(values)
    if packet.type == 3: return max(values)
    if packet.type == 5: return values[0] > values[1]
    if packet.type == 6: return values[0] < values[1]
    if packet.type == 7: return values[0] == values[1]

def product(values):
    p = 1
    for v in values: p*=v
    return p