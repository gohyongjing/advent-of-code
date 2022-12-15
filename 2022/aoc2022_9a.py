def move(coords, direction):
    def move_one(head, tail):
        difference = head[0] - tail[0], head[1] - tail[1]
        tail_change = {(-2, -1): (-1, -1), (-2, 0): (-1, 0), (-2, 1): (-1, 1), 
                       (-1, -2): (-1, -1), (-1, -1): (0, 0), (-1, 0): (0, 0), (-1, 1): (0, 0), (-1, 2): (-1, 1), 
                       (0, -2): (0, -1), (0, -1): (0, 0), (0, 0): (0, 0), (0, 1): (0, 0), (0, 2): (0, 1), 
                       (1, -2): (1, -1), (1, -1): (0, 0), (1, 0): (0, 0), (1, 1): (0, 0), (1, 2): (1, 1), 
                       (2, -1): (1, -1), (2, 0): (1, 0), (2, 1): (1, 1)}[difference]
        return tail[0] + tail_change[0], tail[1] + tail_change[1]
        
    head, tail = coords
    head_change = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}[direction]
    new_head = head[0] + head_change[0], head[1] + head_change[1]
    new_tail = move_one(new_head, tail)
    
    return new_head, new_tail

coords = ((0, 0), (0, 0))
visited = set((coords[1],))
for line in stdin:
    direction, count = line.split(' ')
    for _ in range(int(count)):
        coords = move(coords, direction)
        visited.add(coords[1])
print(len(visited))
