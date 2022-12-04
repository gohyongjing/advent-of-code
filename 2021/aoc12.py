import sys
connections = {}

def is_small(cave):
    return ord('a') <= ord(cave[0]) <= ord('z')

def is_valid(path):
    mult_visits = set(filter(lambda cave: path.count(cave) > 1 and is_small(cave),
                               path))
    if len(mult_visits) > 1:
        return False
    if mult_visits:
        if path.count(mult_visits.pop()) > 2:
            return False
    return True

memo = {}
def pf(connections, current, visited):
    #print(current, visited)
    mult_visits = list(filter(lambda cave: visited[cave] > 1, visited))
    #print(mult_visits)
    if any(visited[cave] > 2 and is_small(cave) for cave in mult_visits):
        return set()
    if sum(1 for cave in mult_visits if is_small(cave)) > 1:
        return set()
    if current == 'end':
        return set((('end',),))
    if (current, tuple(visited.items())) in memo:
        #print((current, tuple(visited.items())), memo[(current, tuple(visited.items()))])
        return memo[(current, tuple(visited.items()))]
    visited = {item[0]: item[1] for item in visited.items()}
    if current not in visited:
        visited[current] = 0
    visited[current] += 1
    
    result = set()
    for cave in connections[current]:
        if cave != 'start':
            paths = pf(connections, cave, visited)
            processed_paths = set()
            for path in paths:
                new_path = (current,) + path
                if is_valid(new_path):
                    processed_paths.add(new_path)
            result = result.union(processed_paths)
    memo[(current, tuple(visited.items()))] = result
    return result
    
for line in ['FK-gc',
'gc-start',
'gc-dw',
'sp-FN',
'dw-end',
'FK-start',
'dw-gn',
'AN-gn',
'yh-gn',
'yh-start',
'sp-AN',
'ik-dw',
'FK-dw',
'end-sp',
'yh-FK',
'gc-gn',
'AN-end',
'dw-AN',
'gn-sp',
'gn-FK',
'sp-FK',
'yh-gc']:
    line = line.strip()
    pt1, pt2 = line.split('-')
    if pt1 not in connections:
        connections[pt1] = set()
    if pt2 not in connections:
        connections[pt2] = set()
    connections[pt1].add(pt2)
    connections[pt2].add(pt1)

#print(connections)
results = pf(connections, 'start', {})
#for result in sorted(results):
    #print(result)
print(len(results))
