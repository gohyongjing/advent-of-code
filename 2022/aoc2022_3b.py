score = 0
priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
group = [None, None, None]
for i, line in enumerate(sys.stdin):
    group[i % 3] = line
    if (i + 1) % 3 == 0:
        for ch in group[0]:
            if ch in group[1] and ch in group[2]:
                score += priorities.index(ch) + 1
                break
print(score)