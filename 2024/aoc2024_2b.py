import sys


def get_input():
  print('Awaiting input (Press Ctrl+D to end input):')
  for line in sys.stdin.readlines():
    yield line[:-1]

def is_increasing(num1: int, num2: int):
  return num1 < num2

def is_safe_level(curr_level:int, next_level: int, should_increase: bool):
  diff = abs(curr_level - next_level) 
  if diff == 0 or diff > 3:
    return False
  if is_increasing(curr_level, next_level) != should_increase:
    return False
  return True

def is_safe_report(nums: list[int]) -> bool:
  if len(nums) == 1:
    return True
  is_first_two_nums_increasing = is_increasing(nums[0], nums[1])
  i = 0
  while i + 1 < len(nums):
    if not is_safe_level(nums[i], nums[i + 1], is_first_two_nums_increasing):
      return False
    i += 1
  return True

num_safe = 0
for line in get_input():
  nums = [int(n) for n in line.split(' ')]
  for i in range(len(nums)):
    if is_safe_report(nums[:i] + nums[i+1:]):
      num_safe += 1
      break

print(num_safe)
