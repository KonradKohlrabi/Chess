from canTakeKing import isCheck
import json

def getColor(y: int, x: int, board: list) -> bool:
    e = board[y][x]
    if e == None:
        return False
    color = list(board[y][x])[2]
    if color == "T":
        return True # White
    else:
        return False # Black

def calcPossibleTurns(array: list, atTurn: str, board: list) -> list:
    possibleTurns = []
    i = 0
    if atTurn == "White":
        for e in array[0]:
            e_type = list(e.id)[0]

            # Tower, Queen
            if e_type == "T" or e_type == "Q":
                x = e.x
                y = e.y
                while True:
                    x += 1
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if board[y][x] == None:
                            possibleTurns.append([i, x, y, e_type])
                        elif not getColor(y, x, board):
                            possibleTurns.append([i, x, y, e_type])
                            break
                        else:
                            break
                    else:
                        break
                x = e.x
                y = e.y
                while True:
                    x -= 1
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if board[y][x] == None:
                            possibleTurns.append([i, x, y, e_type])
                        elif not getColor(y, x, board):
                            possibleTurns.append([i, x, y, e_type])
                            break
                        else:
                            break
                    else:
                        break
                x = e.x
                y = e.y
                while True:
                    y += 1
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if board[y][x] == None:
                            possibleTurns.append([i, x, y, e_type])
                        elif not getColor(y, x, board):
                            possibleTurns.append([i, x, y, e_type])
                            break
                        else:
                            break
                    else:
                        break
                x = e.x
                y = e.y
                while True:
                    y -= 1
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if board[y][x] == None:
                            possibleTurns.append([i, x, y, e_type])
                        elif not getColor(y, x, board):
                            possibleTurns.append([i, x, y, e_type])
                            break
                        else:
                            break
                    else:
                        break

            # Bishop, Queen
            if e_type == "B" or e_type == "Q":
                directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
                for direction in directions:
                    dx, dy = direction
                    x = e.x
                    y = e.y
                    while True:
                        x += dx
                        y += dy
                        if not (x < 0 or x > 7 or y < 0 or y > 7):
                            if board[y][x] == None:
                                possibleTurns.append([i, x, y, e_type])
                            elif not getColor(y, x, board):
                                possibleTurns.append([i, x, y, e_type])
                                break
                            else:
                                break
                        else:
                            break

            # Knight
            if e_type == "N":
                moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
                for move in moves:
                    dx, dy = move
                    x = e.x + dx
                    y = e.y + dy
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y, e_type])

            # Pawn
            if e_type == "P":
                x = e.x
                y = e.y
                y += 1
                if not (x < 0 or x > 7 or y < 0 or y > 7):
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y, e_type])

                if e.onBaseline:
                    y += 1
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if board[y][x] == None:
                            possibleTurns.append([i, x, y, e_type])

                x = e.x
                y = e.y
                moves = [(1, 1), (-1, 1)]
                for move in moves:
                    dx, dy = move
                    x = e.x + dx
                    y = e.y + dy
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if not board[y][x] == None:
                            if not getColor(y, x, board):
                                possibleTurns.append([i, x, y, e_type])

            # King
            if e_type == "K":
                moves = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
                for move in moves:
                    dx, dy = move
                    x = e.x + dx
                    y = e.y + dy
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if not board[y][x] == None:
                            if not getColor(y, x, board):
                                possibleTurns.append([i, x, y, e_type])
            i += 1
    else:
        for e in array[1]:
            e_type = list(e.id)[0]

            # Tower, Queen
            if e_type == "T" or e_type == "Q":
                x = e.x
                y = e.y
                while True:
                    x += 1
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if board[y][x] == None:
                            possibleTurns.append([i, x, y, e_type])
                        elif getColor(y, x, board):
                            possibleTurns.append([i, x, y, e_type])
                            break
                        else:
                            break
                    else:
                        break
                x = e.x
                y = e.y
                while True:
                    x -= 1
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if board[y][x] == None:
                            possibleTurns.append([i, x, y, e_type])
                        elif getColor(y, x, board):
                            possibleTurns.append([i, x, y, e_type])
                            break
                        else:
                            break
                    else:
                        break
                x = e.x
                y = e.y
                while True:
                    y += 1
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if board[y][x] == None:
                            possibleTurns.append([i, x, y, e_type])
                        elif not getColor(y, x, board):
                            possibleTurns.append([i, x, y, e_type])
                            break
                        else:
                            break
                    else:
                        break
                x = e.x
                y = e.y
                while True:
                    y -= 1
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if board[y][x] == None:
                            possibleTurns.append([i, x, y, e_type])
                        elif not getColor(y, x, board):
                            possibleTurns.append([i, x, y, e_type])
                            break
                        else:
                            break
                    else:
                        break

            # Bishop, Queen
            if e_type == "B" or e_type == "Q":
                directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
                for direction in directions:
                    dx, dy = direction
                    x = e.x
                    y = e.y
                    while True:
                        x += dx
                        y += dy
                        if not (x < 0 or x > 7 or y < 0 or y > 7):
                            if board[y][x] == None:
                                possibleTurns.append([i, x, y, e_type])
                            elif not getColor(y, x, board):
                                possibleTurns.append([i, x, y, e_type])
                                break
                            else:
                                break
                        else:
                            break

            # Knight
            if e_type == "N":
                moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
                for move in moves:
                    dx, dy = move
                    x = e.x + dx
                    y = e.y + dy
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y, e_type])

            # Pawn
            if e_type == "P":
                x = e.x
                y = e.y
                y -= 1
                if not (x < 0 or x > 7 or y < 0 or y > 7):
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y, e_type])

                if e.onBaseline:
                    y -= 1
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if board[y][x] == None:
                            possibleTurns.append([i, x, y, e_type])

                x = e.x
                y = e.y
                moves = [(1, -1), (-1, -1)]
                for move in moves:
                    dx, dy = move
                    x = e.x + dx
                    y = e.y + dy
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if not board[y][x] == None:
                            if getColor(y, x, board):
                                possibleTurns.append([i, x, y, e_type])

            # King
            if e_type == "K":
                moves = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
                for move in moves:
                    dx, dy = move
                    x = e.x + dx
                    y = e.y + dy
                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                        if not board[y][x] == None:
                            if getColor(y, x, board):
                                possibleTurns.append([i, x, y, e_type])
            i += 1
    possibleTurns = isCheck(possibleTurns, array, board, atTurn)
    with open("Zwischenspeicher.json", "r") as o:
        board = json.load(o)
    return possibleTurns

