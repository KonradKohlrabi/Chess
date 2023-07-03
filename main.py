board = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None]
]


class Tower:
    def __init__(self, x: int, y: int, number: int, iswhite: bool):
        self.diriktion = ["front", "left", "back", "right"]
        self.jump = False
        self.attack = ["front", "left", "back", "right"]
        self.x = x
        self.y = y
        self.number = number
        self.iswhite = iswhite
        self.id = "T" + str(self.number) + str(self.iswhite)
        board[y][x] = self.id

    def go(self, x, y):
        board[y][x] = self.id
        board[self.y][self.x] = None
        self.x = x
        self.y = y

# White Group
T1True = Tower(0, 0, 1, True)
T2True = Tower(7, 0, 2, True)

# Black Group
T3True = Tower(0, 7, 3, False)
T4True = Tower(7, 7, 4, False)





def calcPossibleTurns(array):
    pass

print(board)
