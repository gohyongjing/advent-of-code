from enum import Enum
import sys


class Instruction(Enum):
  DO = 'do'
  DONT = "don't"
  MUL = "mul"
  NOOP = "noop"

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

def find_dont(line: str, start: int):
  return find_str(line, start, "don't()")

def find_do(line: str, start: int):
  return find_str(line, start, "do()")

def find_product(line: str, start: int):
  index: int = start
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
    
    index = new_index
    return (index, num1 * num2)

  return (-1, None)

def find_nearest_instruction(nearest_dont: int, nearest_do: int, nearest_product: int):
  not_null = list(filter(
    lambda arr: arr[0] != -1,
    [
      [nearest_dont, Instruction.DONT],
      [nearest_do, Instruction.DO],
      [nearest_product, Instruction.MUL],
    ]
  ))

  if len(not_null) == 0:
    return Instruction.NOOP  
  return min(not_null)[1]
  
total_product = 0
enabled = True
for line in get_input():
  nearest_dont = find_dont(line, 0)
  nearest_do = find_do(line, 0)
  nearest_product, product = find_product(line, 0)

  nearest_instruction = find_nearest_instruction(nearest_dont, nearest_do, nearest_product)
  while nearest_instruction != Instruction.NOOP:
    if nearest_instruction == Instruction.DONT:
      enabled = False
      nearest_dont = find_dont(line, nearest_dont)
    elif nearest_instruction == Instruction.DO:
      enabled = True
      nearest_do = find_do(line, nearest_do)
    elif nearest_instruction == Instruction.MUL:
      if product != None and enabled:
        total_product += product
      nearest_product, product = find_product(line, nearest_product)
    else:
      print('unreachable')
      exit()
    
    nearest_instruction = find_nearest_instruction(nearest_dont, nearest_do, nearest_product)

print(total_product)
