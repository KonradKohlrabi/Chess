board = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
]

class Tower:
    def __init__(self, x: int, y: int, number: int, iswhite: bool):
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


class Pawn:
    def __init__(self, x: int, y: int, number: int, iswhite: bool):
        self.x = x
        self.y = y
        self.number = number
        self.iswhite = iswhite
        self.id = "P" + str(self.number) + str(self.iswhite)
        self.onBaseline = True
        board[y][x] = self.id

    def go(self, x, y):
        board[y][x] = self.id
        board[self.y][self.x] = None
        self.x = x
        self.y = y


class Bishop:
    def __init__(self, x: int, y: int, number: int, iswhite: bool):
        self.x = x
        self.y = y
        self.number = number
        self.iswhite = iswhite
        self.id = "B" + str(self.number) + str(self.iswhite)
        board[y][x] = self.id

    def go(self, x, y):
        board[y][x] = self.id
        board[self.y][self.x] = None
        self.x = x
        self.y = y


class Queen:
    def __init__(self, x: int, y: int, number: int, iswhite: bool):
        self.x = x
        self.y = y
        self.number = number
        self.iswhite = iswhite
        self.id = "Q" + str(self.number) + str(self.iswhite)
        board[y][x] = self.id

    def go(self, x, y):
        board[y][x] = self.id
        board[self.y][self.x] = None
        self.x = x
        self.y = y


class King:
    def __init__(self, x: int, y: int, number: int, iswhite: bool):
        self.x = x
        self.y = y
        self.number = number
        self.iswhite = iswhite
        self.id = "K" + str(self.number) + str(self.iswhite)
        board[y][x] = self.id

    def go(self, x, y):
        board[y][x] = self.id
        board[self.y][self.x] = None
        self.x = x
        self.y = y


class Knight:
    def __init__(self, x: int, y: int, number: int, iswhite: bool):
        self.x = x
        self.y = y
        self.number = number
        self.iswhite = iswhite
        self.id = "N" + str(self.number) + str(self.iswhite)
        board[y][x] = self.id

    def go(self, x, y):
        board[y][x] = self.id
        board[self.y][self.x] = None
        self.x = x
        self.y = y