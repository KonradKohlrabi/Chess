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


class Pawn:
    def __init__(self, x: int, y: int, number: int, iswhite: bool):
        self.direction = ["front"]
        self.jump = False
        self.attack = ["left-front", "right-front"]
        self.x = x
        self.y = y
        self.number = number
        self.iswhite = iswhite
        self.id = "P" + str(self.number) + str(self.iswhite)
        board[y][x] = self.id

    def go(self, x, y):
        board[y][x] = self.id
        board[self.y][self.x] = None
        self.x = x
        self.y = y


class Bishop:
    def __init__(self, x: int, y: int, number: int, iswhite: bool):
        self.direction = ["left-front", "right-front", "left-back", "right-back"]
        self.jump = False
        self.attack = ["left-front", "right-front", "left-back", "right-back"]
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
        self.direction = [
            "left-front",
            "right-front",
            "left-back",
            "right-back",
            "front",
            "left",
            "back",
            "right",
        ]
        self.jump = False
        self.attack = [
            "left-front",
            "right-front",
            "left-back",
            "right-back",
            "front",
            "left",
            "back",
            "right",
        ]
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
        self.direction = [
            "left-front",
            "right-front",
            "left-back",
            "right-back",
            "front",
            "left",
            "back",
            "right",
        ]
        self.jump = False
        self.attack = [
            "left-front",
            "right-front",
            "left-back",
            "right-back",
            "front",
            "left",
            "back",
            "right",
        ]
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
        self.direction = []
        self.jump = False
        self.attack = []
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