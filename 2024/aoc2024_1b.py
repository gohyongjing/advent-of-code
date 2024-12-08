import sys


list1: list[int] = []
count: dict[int, int] = {}

print('Awaiting input...')
for line in sys.stdin:
  stripped = line.strip()
  if stripped == '':
    break
  num1, num2 = (int(n) for n in stripped.split('  '))
  list1.append(num1)
  count[num2] = count.get(num2, 0) + 1


total_score = 0
for num in list1:
  total_score += num * count.get(num, 0)

print(total_score)

