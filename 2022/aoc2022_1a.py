max_cal = 0
curr_cal = 0
for line in sys.stdin:
    if line == "\n":
        max_cal = max(max_cal, curr_cal)
        curr_cal = 0
    else:
        curr_cal += int(line)
max_cal = max(max_cal, curr_cal)

print(max_cal)