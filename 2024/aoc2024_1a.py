import sys


list1: list[int] = []
list2: list[int] = []

print('Awaiting input...')
for line in sys.stdin:
  stripped = line.strip()
  if stripped == '':
    break
  item1, item2 = stripped.split('  ')
  list1.append(int(item1))
  list2.append(int(item2))

list1.sort()
list2.sort()

total_sum = 0
for num1, num2 in zip(list1, list2):
  total_sum += abs(num1 - num2)

print(total_sum)
