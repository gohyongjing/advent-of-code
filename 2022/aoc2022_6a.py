buffer = [None] * 4

for i, char in enumerate(stdin.readline()):
    buffer[i % 4] = char
    if i >= 3 and len(set(buffer)) == 4 :
        print(i + 1)
        break