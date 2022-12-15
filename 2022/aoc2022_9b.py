def move(coords, direction):
    def move_one(head, tail):
        difference = head[0] - tail[0], head[1] - tail[1]
        tail_change = {(-2, -2): (-1, -1), (-2, -1): (-1, -1), (-2, 0): (-1, 0), (-2, 1): (-1, 1), (-2, 2): (-1, 1), 
                       (-1, -2): (-1, -1), (-1, -1): (0, 0), (-1, 0): (0, 0), (-1, 1): (0, 0), (-1, 2): (-1, 1), 
                       (0, -2): (0, -1), (0, -1): (0, 0), (0, 0): (0, 0), (0, 1): (0, 0), (0, 2): (0, 1), 
                       (1, -2): (1, -1), (1, -1): (0, 0), (1, 0): (0, 0), (1, 1): (0, 0), (1, 2): (1, 1), 
                       (2, -2): (1, -1), (2, -1): (1, -1), (2, 0): (1, 0), (2, 1): (1, 1), (2, 2): (1, 1)}[difference]
        tail[0] += tail_change[0]
        tail[1] += tail_change[1]
    
    head_change = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}[direction]
    coords[0] = coords[0][0] + head_change[0], coords[0][1] + head_change[1]
    for i in range(9):
        move_one(coords[i], coords[i + 1])

coords = [[0, 0] for _ in range(10)]
visited = set((tuple(coords[9]),))
for line in stdin:
    direction, count = line.split(' ')
    for _ in range(int(count)):
        move(coords, direction)
        visited.add(tuple(coords[9]))
print(len(visited))
