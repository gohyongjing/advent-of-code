
folds = []
dots = set()
folding = False
file = open("aoc input.txt", "r")
for line in file:
    line = line.strip()    
    if not line:
        folding = True
        continue
    if folding:
        direction, coord = line.split(' ')[-1].split('=')
        folds.append((direction, int(coord)))
    else:
        dots.add(tuple(int(i) for i in line.split(',')))

def do_fold(dots, fold):
    direction, coord = fold
    index = 0 if direction == 'x' else 1
    new_dots = set()
    for dot in dots:
        if dot[index] > coord:
            new_dot = [None, None]
            new_dot[index] = coord - (dot[index] - coord)
            new_dot[(index + 1) % 2] = dot[(index + 1) % 2] 
            new_dots.add(tuple(new_dot))
        else:
            new_dots.add(dot)
    return new_dots

    
print(dots, folds)

for fold in folds:
    dots = do_fold(dots, fold)


print(sorted(dots), len(dots))
for y in range(100):
    line = ''
    for x in range(100):
        line += ('#' if (x, y) in dots else '.')
    print(line)
        
        
