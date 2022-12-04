from copy import deepcopy

class SnailNumber:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"[{self.left}, {self.right}]"

    def __repr__(self):
        return self.__str__()

    def add(self, other):
        new = SnailNumber(deepcopy(self), deepcopy(other))
        new.reduce()
        return new

    def reduce(self):
        done = False
        while not done:
            #print('reducing ' , self)
            done = True
            exploded = self.check_explode()
            if exploded:
                done = False
            else:
                splited = self.check_split()
                if splited:
                    done = False

    def check_explode(self):
        def check(number, layer):
            #returns whether it explodes
            if isinstance(number, int):
                return False, {}
            if layer == 5:
                return True, number.get_first_pair()
            else:
                exploded, direction = check(number.left, layer + 1)
                #if 'left' in direction :
                    #print(number, 'from left: ', exploded, direction)
                if 'right' in direction:
                    if isinstance(number.right, int):
                        number.right += direction['right']
                    else:
                        number.right.add_int('left', direction['right'])
                    direction.pop('right')
                    if 'left' in direction:
                        number.left = 0
                    return exploded, direction
                elif 'left' in direction:
                    #direction = {'right': direction['left']}
                    return exploded, direction
                elif exploded:
                    return exploded, direction
            
                exploded, direction = check(number.right, layer + 1)
                #if 'left' in direction :
                    #print(number, 'from right: ', exploded, direction)
                if 'left' in direction:
                    if isinstance(number.left, int):
                        number.left += direction['left']
                    else:
                        number.left.add_int('right', direction['left'])
                    direction.pop('left')
                    if 'right' in direction:
                        number.right = 0
                    return exploded, direction
                elif 'right' in direction:
                    #direction = {'left': direction['right']}
                    return exploded, direction
                else:
                    return exploded, direction
                    
        exploded, direction = check(self, 1)
        return exploded

    def get_first_pair(self):
        if isinstance(self.left, int):
            if isinstance(self.right, int):
                return {'left': self.left, 'right': self.right}
            else:
                return self.right.get_first_pair()
        else:
            return self.left.get_first_pair()

    
    def add_int(self, direction, value):
        if direction == 'left':
            if isinstance(self.left, int):
                self.left += value
                return
            self.left.add_int('left', value)
        if direction == 'right':
            if isinstance(self.right, int):
                self.right += value
                return
            self.right.add_int('right', value)


    def check_split(self):
        if isinstance(self.left, int):
            if self.left >=10:
                rounded_down = self.left // 2
                self.left = SnailNumber(rounded_down, self.left - rounded_down)
                return True
        else:
            if self.left.check_split():
                return True
        if isinstance(self.right, int):
            if self.right >=10:
                rounded_down = self.right // 2
                self.right = SnailNumber(rounded_down, self.right - rounded_down)
                return True
            return False
        else:
            return self.right.check_split()

    def get_magnitude(self):
        left_mag = self.left if isinstance(self.left, int) else (self.left.get_magnitude())
        right_mag = self.right if isinstance(self.right, int) else self.right.get_magnitude()
        return left_mag * 3 + right_mag * 2     

def parse(string):
    if '[' == string[0]:
        count = 0
        index = 1
        while True:
            ch = string[index]
            if ch == ',' and count == 0:
                break
            elif ch == '[':
                count += 1
            elif ch == ']':
                count -= 1
            index += 1
        left = parse(string[1 : index])
        right = parse(string[index+1 : -1])
        return SnailNumber(left, right)
    else:
        return int(string)

numbers = []

file = open("aoc input.txt", "r")
for i, line in enumerate(file):
    line = line.strip()
    numbers.append(parse(line))

'''
result = numbers[0]
for number in numbers[1:]:
    #print('adding ' + str(number)) 
    result = result.add(number)
    #print('result ' + str(result))

print(result, result.get_magnitude())
'''


largest = 0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            total = numbers[i].add(numbers[j])
            mag = total.get_magnitude()
            #print(i, j, total, mag)
            if mag > largest:
                largest = mag

print(largest)
