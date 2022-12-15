class Worry:
    max_level = 1
    def __init__(self, level):
        self.level = level
    
    def __add__(self, other):
        return Worry((self.level + other.level) % Worry.max_level)
    
    def __mul__(self, other):
        return Worry((self.level * other.level) % Worry.max_level)
    
    def __mod__(self, other):
        return Worry(self.level % other.level)
    
    def __eq__(self, other):
        return self.level == other.level
        
class Monkey:
    def __init__(self, details):
        self.id = details['monkey_id']
        self.items = details['items']
        self.operation = details['operation']
        self.test = details['test']
        self.action_on_true = details['action_on_true']
        self.action_on_false = details['action_on_false']
        self.inspections = 0
    
    def operate(self, item):
        operand1 = item if self.operation[0] == 'old' else Worry(int(self.operation[0]))
        operand2 = item if self.operation[2] == 'old' else Worry(int(self.operation[2]))
        return operand1 + operand2 if self.operation[1] == '+' else operand1 * operand2
    
    def test_item(self, item):
        return (item % self.test) == Worry(0)
    
    def act(self):
        results = []
        self.inspections += len(self.items)
        for item in self.items:
            item = self.operate(item)
            if self.test_item(item):
                results.append((item, self.action_on_true))
            else:
                results.append((item, self.action_on_false))
        self.items = []
        return results
        
    def add_item(self, item):
        self.items.append(item)
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return str((self.id, self.items, self.operation, \
                    self.test, self.action_on_true, self.action_on_false))

monkeys = []
details = {}
for line in stdin:
    line = line.strip()
    if line.split(':')[0].split(' ')[0] == 'Monkey':
        details['monkey_id'] = int(line.split(':')[0].split(' ')[1])
    elif line.split(':')[0] == 'Starting items':
        details['items'] = [Worry(int(n)) for n in line.split(': ')[1].split(', ')]
    elif line.split(':')[0] == 'Operation':
        details['operation'] = line.split(': ')[1].split(' = ')[1].split(' ')
    elif line.split(':')[0] == 'Test':
        test = int(line.split(': ')[1].split(' ')[-1])
        details['test'] = Worry(test)
        Worry.max_level *= test
    elif line.split(':')[0] == 'If true':
        details['action_on_true'] = int(line.split(': ')[1].split(' ')[-1])
    elif line.split(':')[0] == 'If false':
        details['action_on_false'] = int(line.split(': ')[1].split(' ')[-1])
        monkeys.append(Monkey(details))

for i in range(10000):
    for monkey in monkeys:
        for item, target in monkey.act():
            monkeys[target].add_item(item)


inspections = sorted([monkey.inspections for monkey in monkeys])
print(inspections[-1] * inspections[-2])
