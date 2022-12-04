class Node:
    def __init__(self, coords, val):
        self.coords = coords
        self.val = val
        self.start_dist = float('inf')
        self.end_dist = float('inf')
        self.prev = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"({self.coords[0]} {self.coords[1]}) {self.val} Start:{self.start_dist} End:{self.end_dist}"

class CustomSet:
    def __init__(self):
        self.items = set()

    def add(self, item):
        self.items.add(item)

    def pop(self):
        result = min(self.items, key = lambda item: item.start_dist + item.end_dist)
        self.items.remove(result)
        return result

    def len(self):
        return len(self.items)

def get_neighbours(cell, grid):
    x, y = cell.coords
    result = []
    for x1, y1 in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
        if 0 <= x1 < len(grid[0]) and 0 <= y1 < len(grid):
            result.append(grid[y1][x1])
    return result


start_nodes = []
file = open("aoc input.txt", "r")
for y, line in enumerate(file):
    start_nodes.append([Node((x, y), int(val)) for x, val in enumerate(line.strip())])


nodes = [[None] * 5 * len(start_nodes[0]) for _ in range(5 * len(start_nodes))]
for y in range(5):
    for x in range(5):
        for row in start_nodes:
            for node in row:
                new_y = node.coords[1] + y * len(start_nodes)
                new_x = node.coords[0] + x * len(start_nodes[0])
                new_val = node.val + x + y
                if new_val > 9:
                    new_val -= 9
                nodes[new_y][new_x] = Node((new_x, new_y), new_val)
'''
for y in range(len(nodes)):
    line = ''
    for x in range(len(nodes[0])):
        line += str(nodes[y][x].val)
    print(line)'''


end_x, end_y = len(nodes[0]) - 1, len(nodes) - 1
end_node = nodes[end_y][end_x]
for row in nodes:
    for node in row:
        x, y = node.coords
        node.end_dist = end_y - y + end_x - x 

to_check = CustomSet()
start_node = nodes[0][0]
start_node.start_dist = 0
to_check.add(start_node)
checked = set()

while to_check.len() > 0:
    node = to_check.pop()
    if node.coords == (end_x, end_y):
        break
    for neighbour_node in get_neighbours(node, nodes):
        if node.start_dist + neighbour_node.val < neighbour_node.start_dist:
            neighbour_node.prev = node
            neighbour_node.start_dist = node.start_dist + neighbour_node.val
        if neighbour_node not in checked:
            to_check.add(neighbour_node)
    checked.add(node)
    

node = end_node
while node:
    print(node)
    node = node.prev

print(end_node.start_dist)


'''

def path_cost(path):
    return sum(grid[y][x] for x, y in path)

    
memo = {}
def pathfind(curr, target, visited):
    if curr == target:
        return [target]
    if curr in visited:
        return []
    else:
        visited = visited.union(set((curr,)))
        paths = []
        for neighbour in get_neighbours(curr):
            path = pathfind(neighbour, target, visited)
            if path:
                path.append(curr)
                paths.append(path)
        result = []
        if paths:
            result = min(paths, key = lambda path: path_cost(path))
        return result

result = pathfind((0,0), (len(grid[0])-1, len(grid)-1), set())
print(result)
print(path_cost(result[:-1]))'''


