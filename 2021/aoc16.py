file = open("aoc input.txt", "r")


hexa_table = {'0': '0000',
              '1': '0001',
              '2': '0010',
              '3': '0011',
              '4': '0100',
              '5': '0101',
              '6': '0110',
              '7': '0111',
              '8': '1000',
              '9': '1001',
              'A': '1010',
              'B': '1011',
              'C': '1100',
              'D': '1101',
              'E': '1110',
              'F': '1111'}
              
def decode(hexa):
    def mapper(hexa):
        return hexa_table[hexa]
    return "".join(map(mapper, hexa))

def binary_to_dec(binary):
    result = 0
    while binary:
        result *= 2
        if binary[0] == '1':
            result += 1
        binary = binary[1:]
    return result


def solve(line):
    instr = {}
    version = binary_to_dec(line[:3])
    line = line[3:]
    instr['version'] = version
    type_id = binary_to_dec(line[:3])
    line = line[3:]
    instr['type_id'] = type_id
    if type_id == 4:
        num = ''
        digit = '1'
        while digit[0] == '1':
            digit = line[:5]
            line = line[5:]
            num += digit[1:]
        instr['literal'] = binary_to_dec(num)
        return instr, line
    else:
        length_id = line[0]
        line = line[1:]
        instr['length_id'] = length_id
        if length_id == '0':
            length = binary_to_dec(line[:15])
            line = line[15:]
            instr['length'] = length
            packets = line[:length]
            line = line[length:]
            sub_packets = []
            rem_line = line
            while packets:
                p, packets = solve(packets)
                sub_packets.append(p)
            instr['sub_packets'] = sub_packets
            return instr, line
        else:
            length = binary_to_dec(line[:11])
            line = line[11:]
            instr['length'] = length
            sub_packets = []
            for _ in range(length):
                p, line = solve(line)
                sub_packets.append(p)
            instr['sub_packets'] = sub_packets
            return instr, line

for _, line in enumerate(file):
    instructions, remaining = solve(decode(line))
    print(instructions)
    print('remaining: ' + remaining)

    v_count = 0
    unsolved = [instructions]
    while unsolved:
        instr = unsolved.pop()
        v_count += instr['version']
        if 'sub_packets' in instr:
            for sub_packet in instr['sub_packets']:
                unsolved.append(sub_packet)
    print(v_count)

    def solve2(instruction):
        def product(packets):
            result = 1
            for p in packets:
                result *= p
            return result

        if instruction['type_id'] == 4:
            return instruction['literal']
        
        fn = {0: lambda packets: sum(solve2(packet) for packet in packets),
              1: lambda packets: product(solve2(packet) for packet in packets),
              2: lambda packets: min(solve2(packet) for packet in packets),
              3: lambda packets: max(solve2(packet) for packet in packets),
              5: lambda packets: 1 if solve2(packets[0]) > solve2(packets[1]) else 0,
              6: lambda packets: 1 if solve2(packets[0]) < solve2(packets[1]) else 0,
              7: lambda packets: 1 if solve2(packets[0]) == solve2(packets[1]) else 0}[instruction['type_id']]
        return fn(instruction['sub_packets'])

    print(solve2(instructions))
