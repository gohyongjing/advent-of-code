stacks = [[] for _ in range(9)]

for i, line in enumerate(sys.stdin):
    if i < 8:
        for j in range(9):
            if line[j * 4 + 1] != ' ':
                stacks[j].insert(0, line[j * 4 + 1])
    elif i > 9:
        _, count, _, src, _, dest = line.split(' ')
        temp = []
        for _ in range(int(count)):
            temp.append(stacks[int(src) - 1].pop())
        for _ in range(int(count)): 
            stacks[int(dest) - 1].append(temp.pop())

print("".join(arr[-1] for arr in stacks))