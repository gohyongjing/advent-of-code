class Pos:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        
    def __eq__(self, other):
        return self.y == other.y and self.x == other.x
    
    def __hash__(self):
        return hash((self.y, self.x))
    
    def get_neighbours(self, grid):
        result = []
        for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_y = self.y + direction[0]
            new_x = self.x + direction[1]
            if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]):
                result.append(Pos(new_y, new_x))
        return result

class Node:
    def __init__(self, pos, steps, grid):
        self.pos = pos
        self.steps = steps
        self.grid = grid

    def get_height(self, pos):
        ch = self.grid[pos.y][pos.x]
        if ch in ('S', 'E'):
            ch = {'S': 'a', 'E': 'z'}[ch]
        return ord(ch)
    
    def get_neighbours(self):
        results = []
        curr_height = self.get_height(self.pos)
        for neighbour_pos in self.pos.get_neighbours(self.grid):
            neighbour_height = self.get_height(neighbour_pos)
            if neighbour_height - curr_height <= 1:
                results.append(Node(neighbour_pos, self.steps + 1, self.grid))
        return results

grid = [line.strip() for line in stdin]
visited = set()
frontier = []
for y, line in enumerate(grid):
    for x, ch in enumerate(line):
        if ch == 'S':
            frontier.append(Node(Pos(y, x), 0, grid))

while frontier:
    node = frontier.pop(0)
    if node.pos in visited:
        continue
    elif grid[node.pos.y][node.pos.x] == 'E':
        print(node.steps)
        break
    visited.add(node.pos)    
    for neighbour in node.get_neighbours():
        frontier.append(neighbour)
