count = 0
for line in sys.stdin:
    section1, section2 = line.split(',')
    start1, end1 = (int(i) for i in section1.split('-'))
    start2, end2 = (int(i) for i in section2.split('-'))
    if (start1 >= start2 and end1 <= end2) \
    or (start2 >= start1 and end2 <= end1):
        count +=1
print(count)