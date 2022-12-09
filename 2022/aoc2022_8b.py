def reverse(grid):
    return [row[::-1] for row in grid]

def transpose(grid):
    result = []
    for x in range(len(grid[0])):
        result.append([grid[y][x] for y in range(len(grid))])
    return result

def get_view_on_left(grid):
    result = [[[0] * 10 for _ in row] for row in grid]
    for y, row in enumerate(grid):
        for x in range(len(row) - 1):
            for height in range(10):
                if x == 0 or row[x] >= height:
                    result[y][x + 1][height] = 1
                else:
                    result[y][x + 1][height] = result[y][x][height] + 1
    return result

def get_view_on_right(grid):
    return reverse(get_view_on_left(reverse(grid)))

def get_view_on_top(grid):
    return transpose(get_view_on_left(transpose(grid)))

def get_view_on_bottom(grid):
    return transpose(get_view_on_right(transpose(grid)))

grid = [[int(i) for i in line.strip()] for line in stdin]
view_on_left = get_view_on_left(grid)
view_on_right = get_view_on_right(grid)
view_on_top = get_view_on_top(grid)
view_on_bottom = get_view_on_bottom(grid)

highest_score = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        score = (view_on_left[y][x][grid[y][x]] * \
                view_on_right[y][x][grid[y][x]] * \
                view_on_top[y][x][grid[y][x]] * \
                view_on_bottom[y][x][grid[y][x]])
        highest_score = max(highest_score, score)
print(highest_score)
