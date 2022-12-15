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
        operand1 = item if self.operation[0] == 'old' else int(self.operation[0])
        operand2 = item if self.operation[2] == 'old' else int(self.operation[2])
        return operand1 + operand2 if self.operation[1] == '+' else operand1 * operand2
        
    def get_bored(self, item):
        return item // 3
    
    def test_item(self, item):
        return not (item % self.test)
    
    def act(self):
        results = []
        self.inspections += len(self.items)
        for item in self.items:
            item = self.operate(item)
            item = self.get_bored(item)
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
        details['items'] = [int(n) for n in line.split(': ')[1].split(', ')]
    elif line.split(':')[0] == 'Operation':
        details['operation'] = line.split(': ')[1].split(' = ')[1].split(' ')
    elif line.split(':')[0] == 'Test':
        details['test'] = int(line.split(': ')[1].split(' ')[-1])
    elif line.split(':')[0] == 'If true':
        details['action_on_true'] = int(line.split(': ')[1].split(' ')[-1])
    elif line.split(':')[0] == 'If false':
        details['action_on_false'] = int(line.split(': ')[1].split(' ')[-1])
        monkeys.append(Monkey(details))
        
for _ in range(20):
    for monkey in monkeys:
        for item, target in monkey.act():
            monkeys[target].add_item(item)

inspections = sorted([monkey.inspections for monkey in monkeys])
print(inspections[-1] * inspections[-2])
