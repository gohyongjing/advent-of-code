class CPU:
    def __init__(self):
        self.x = 1
        self.cycle = 0
        self.signal_strengths = []
        self.screen = [[''] * 40 for _ in range(6)]
    
    def draw(self):
        y = self.cycle // 40
        x = self.cycle % 40
        if abs(x - self.x) <= 1:
            self.screen[y][x] = '#'
        else:
            self.screen[y][x] = '.'
    
    def tick(self):
        self.draw()
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
for row in cpu.screen:
    print("".join(row))
