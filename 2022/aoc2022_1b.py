top_cals = [0, 0, 0]
curr_cal = 0
for line in sys.stdin:
    if line == "\n":
        min_top = min(top_cals)
        if curr_cal > min_top:
            top_cals[top_cals.index(min_top)] = curr_cal
        curr_cal = 0
    else:
        curr_cal += int(line)
        
min_top = min(top_cals)
if curr_cal > min_top:
    top_cals[top_cals.index(min_top)] = curr_cal

print(sum(top_cals))