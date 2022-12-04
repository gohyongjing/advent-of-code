scanners = []
file = open("aoc input.txt", "r")
for i, line in enumerate(file):
    line = line.strip()
    if line == '':
        scanners.append(scanner)
    elif line[:3] == '---':
        scanner = []
    else:
        scanner.append([int(i) for i in line.split(',')])
scanners.append(scanner)

for scanner in scanners:
    print(scanner)
