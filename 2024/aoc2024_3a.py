import sys


def get_input():
  print('Awaiting input (Press Ctrl+D to end input):')
  for line in sys.stdin.readlines():
    yield line[:-1]

def find_str(line: str, start: int, target: str, allow_skip: bool = True) -> int:
  for i in range(start, len(line)):
    if line[i : i + len(target)] == target:
      return i + len(target)
    if not allow_skip:
      return -1
  return -1

def find_num(line: str, start: int) -> tuple[int, int | None]:
  number = None
  for end in range(start + 1, len(line)):
    try:
      number = int(line[start : end])
    except Exception:
      return end - 1, number
  return len(line) - 1, number

total_product = 0
for line in get_input():
  index: int = 0
  while index != -1:
    index = find_str(line, index, 'mul(')
    if index == -1:
      break
    
    new_index, num1 = find_num(line, index)
    if num1 == None:
      continue
    else:
      index = new_index
    
    new_index = find_str(line, index, ',', allow_skip=False)
    if new_index == -1:
      continue
    else:
      index = new_index
    
    new_index, num2 = find_num(line, index)
    if num2 == None:
      continue
    else:
      index = new_index
    
    new_index = find_str(line, index, ')', allow_skip=False)
    if new_index == -1:
      continue
    else:
      index = new_index
    total_product += num1 * num2

print(total_product)
