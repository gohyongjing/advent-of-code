buffer = [None] * 14

for i, char in enumerate(stdin.readline()):
    buffer[i % 14] = char
    if i >= 3 and len(set(buffer)) == 14 :
        print(i + 1)
        break