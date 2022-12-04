file = open("aoc input.txt", "r")

def solve(region_start, region_end, acceleration, speed_range):
    answers = []
    for u in speed_range:
        s = 0
        vel = u
        for step in range(1000):
            if region_start <= s <= region_end:
                answers.append(u)
                break
            s += vel
            vel = acceleration(vel)
    return answers

def show_trajectory(x, y):
    x_pos = 0
    y_pos = 0
    plots = []
    for i in range(1000):
        plots.append((x_pos, y_pos))
        x_pos += x
        y_pos += y
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1
        y -= 1
    print(plots)


for i, line in enumerate(file):    
    target_x, target_y = line[13:].strip().split(' ')
    x1, x2 = (int(i) for i in target_x[:-1][2:].split('..'))
    y1, y2 = (int(i) for i in target_y[2:].split('..'))
    print(x1, x2, y1, y2)
    results_y = solve(y1, y2, acceleration = lambda u: u - 1, speed_range = range(-1000, 1000, 1))
    results_x = solve(x1, x2, acceleration = lambda u: u if u == 0 else (u - 1 if u > 0 else u + 1), speed_range = range(1000))
    print(results_x)
    print(results_y)
    print(len(results_x), len(results_y))
    print(len(results_x) * len(results_y))

    results = set()
    for ux in range(126):
        for uy in range(-200, 200):
            vx = ux
            vy = uy
            sx = 0
            sy = 0
            while sx <= x2 and sy >= y1:
                if sx >= x1 and sy <= y2:
                    results.add((ux, uy))
                sx += vx
                if vx > 0:
                    vx -= 1
                sy += vy
                vy -= 1
                
    print(len(results))
            
