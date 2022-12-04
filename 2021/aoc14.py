table = {}

def add_to_dictionary(item, dictionary, quantity):
    if item not in dictionary:
        dictionary[item] = 0
    dictionary[item] += quantity

def process(seq, table):
    new_seq = {}
    for pair in seq:
        if pair in table:
            add_to_dictionary(pair[0] + table[pair], new_seq, seq[pair])
            add_to_dictionary(table[pair] + pair[1], new_seq, seq[pair])
        else:
            add_to_dictionary(pair, new_seq, seq[pair])
    return new_seq

        
file = open("aoc input.txt", "r")
for i, line in enumerate(file):
    if i > 1:
        key, value = line.strip().split(' -> ')
        table[key] = value
    elif i == 0:
        line = line.strip()
        first = line[0]
        last = line[-1]
        sequence = {}
        for i in range(len(line)-1):
            add_to_dictionary(line[i] + line[i+1], sequence, 1)
        
print(sequence)
print(table)

for stage in range(1, 41):
    print(stage)
    sequence = process(sequence, table)
    #print(sequence)


counts = {first: 1, last: 1}
#print(counts, sequence)
for pair in sequence:
    add_to_dictionary(pair[0], counts, sequence[pair])
    add_to_dictionary(pair[1], counts, sequence[pair])
counts = {item[0]: item[1] / 2 for item in counts.items()}

print(list(sorted(counts.items(), key = lambda item: item[1])))
