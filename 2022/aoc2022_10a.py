class CPU:
    def __init__(self):
        self.x = 1
        self.cycle = 0
        self.signal_strengths = []
    
    def tick(self):
        self.cycle += 1
        self.signal_strengths.append(self.x * self.cycle)
        
    def addX(self, value):
        self.tick()
        self.tick()
        self.x += value
        
    def noop(self):
        self.tick()
        
    def execute(self, instruction):
        args = instruction.split(' ')
        if args[0] == 'noop':
            self.noop()
        if args[0] == 'addx':
            self.addX(int(args[1]))
        
cpu = CPU()
for line in stdin:
    cpu.execute(line.strip())
strengths = cpu.signal_strengths
result = 0
for i in [20, 60, 100, 140, 180, 220]:
    result += strengths[i - 1]
print(result)
