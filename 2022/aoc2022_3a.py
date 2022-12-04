score = 0
priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for line in sys.stdin:
    compartment1 = line[:len(line) // 2]
    for ch in line[len(line) // 2:]:
        if ch in compartment1:
            score += priorities.index(ch) + 1
            break
print(score)