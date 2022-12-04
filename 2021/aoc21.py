
class Player():
    def __init__(self, pos):
        self.pos = pos
        self.score = 0

    def move(self, value):
        self.pos = ((self.pos - 1 + value) % 10) + 1
        self.score += self.pos


def roll_die():
    curr = 1
    while True:
        yield curr
        curr += 1
        if curr > 100:
            curr = 1

file = open("aoc input.txt", "r")
players = [None, None]
for i, line in enumerate(file):
   players[i] = Player(int(line.split(': ')[1]))


die = roll_die()
rolls = 0
ended = False
while not ended:
    for i, player in enumerate(players):
        player.move(next(die) + next(die) + next(die))
        rolls += 3
        if player.score >= 21:
            print(players[(i + 1) % 2].score, rolls, players[(i + 1) % 2].score * rolls)
            ended = True
            break

