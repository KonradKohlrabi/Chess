from classes import Bishop, Tower, Pawn, King, Knight, Queen, board

atTurn = "White"
player = [
    [
        Tower(0, 0, 1, True),
        Tower(7, 0, 2, True),
        Pawn(0, 1, 1, True),
        Pawn(1, 1, 2, True),
        Pawn(2, 1, 3, True),
        Pawn(3, 1, 4, True),
        Pawn(4, 1, 5, True),
        Pawn(5, 1, 6, True),
        Pawn(6, 1, 7, True),
        Pawn(7, 1, 8, True),
        Bishop(2, 0, 1, True),
        Bishop(5, 0, 2, True),
        Queen(3, 0, 1, True),
        King(4, 0, 1, True),
        Knight(1, 0, 1, True),
        Knight(6, 0, 2, True),
    ],
    [
        Tower(0, 7, 1, False),
        Tower(7, 7, 2, False),
        Pawn(0, 6, 1, False),
        Pawn(1, 6, 2, False),
        Pawn(2, 6, 3, False),
        Pawn(3, 6, 4, False),
        Pawn(4, 6, 5, False),
        Pawn(5, 6, 6, False),
        Pawn(6, 6, 7, False),
        Pawn(7, 6, 8, False),
        Bishop(2, 7, 1, False),
        Bishop(5, 7, 2, False),
        Queen(3, 7, 1, False),
        King(4, 7, 1, False),
        Knight(1, 7, 1, False),
        Knight(6, 7, 2, False),
    ],
]


def calcPossibleTurns(array: list, atTurn: bool, board: list) -> list:
    possibleTurns = []
    i = 0
    if atTurn == "White":
        for e in array[0]:
            e_type = list(e.id)[0]
            # Tower
            if e_type == "T":
                x = e.x
                y = e.y
                while True:
                    x += 1
                    if x == 8:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
                x = e.x
                y = e.y
                while True:
                    x -= 1
                    if x == -1:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
                x = e.x
                y = e.y
                while True:
                    y += 1
                    if y == 8:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
                x = e.x
                y = e.y
                while True:
                    y -= 1
                    if y == -1:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
            # Bishop
            if e_type == "B":
                x = e.x
                y = e.y
                while True:
                    x += 1
                    y += 1
                    if x == -1 or y == -1 or x == 8 or y == 8:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
                x = e.x
                y = e.y
                while True:
                    x -= 1
                    y += 1
                    if x == -1 or y == -1 or x == 8 or y == 8:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
                x = e.x
                y = e.y
                while True:
                    x += 1
                    y -= 1
                    if x == -1 or y == -1 or x == 8 or y == 8:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
                x = e.x
                y = e.y
                while True:
                    x -= 1
                    y -= 1
                    if x == -1 or y == -1 or x == 8 or y == 8:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
            # Queen
            if e_type == "Q":
                x = e.x
                y = e.y
                while True:
                    x += 1
                    y += 1
                    if x == -1 or y == -1 or x == 8 or y == 8:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
                x = e.x
                y = e.y
                while True:
                    x -= 1
                    y += 1
                    if x == -1 or y == -1 or x == 8 or y == 8:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
                x = e.x
                y = e.y
                while True:
                    x += 1
                    y -= 1
                    if x == -1 or y == -1 or x == 8 or y == 8:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
                x = e.x
                y = e.y
                while True:
                    x -= 1
                    y -= 1
                    if x == -1 or y == -1 or x == 8 or y == 8:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
                x = e.x
                y = e.y
                while True:
                    x += 1
                    if x == 8:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
                x = e.x
                y = e.y
                while True:
                    x -= 1
                    if x == -1:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
                x = e.x
                y = e.y
                while True:
                    y += 1
                    if y == 8:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break
                x = e.x
                y = e.y
                while True:
                    y -= 1
                    if y == -1:
                        break
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])
                    else:
                        possibleTurns.append([i, x, y])
                        break

        i += 1
    else:
        for e in array[1]:
            pass
    return possibleTurns

for y in board:
    print(y)
