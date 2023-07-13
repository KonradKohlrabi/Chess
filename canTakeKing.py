def canTakeKing(board: list, atTurn: str) -> bool:
    if atTurn == "White": # White has pullt. Now at turn is Black
        indexY = 0
        for yFor in board:
            indexX = 0
            for e in yFor:
                if not e == None:
                    if list(e)[2] == "F": # Check if its a black figure
                        e_type = list(e)[0]

                        # Tower, Queen
                        if e_type == "T" or e_type == "Q":
                            x = indexX
                            y = indexY
                            while True:
                                x += 1
                                if not (x < 0 or x > 7 or y < 0 or y > 7):
                                    if not board[y][x] == None:
                                        if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "T": # Check if its the white king
                                            return True
                                else:
                                    break
                            x = indexX
                            y = indexY
                            while True:
                                x -= 1
                                if not (x < 0 or x > 7 or y < 0 or y > 7):
                                    if not board[y][x] == None:
                                        if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "T": # Check if its the white king
                                            return True
                                else:
                                    break
                            x = indexX
                            y = indexY
                            while True:
                                y += 1
                                if not (x < 0 or x > 7 or y < 0 or y > 7):
                                    if not board[y][x] == None:
                                        if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "T": # Check if its the white king
                                            return True
                                else:
                                    break
                            x = indexX
                            y = indexY
                            while True:
                                y -= 1
                                if not (x < 0 or x > 7 or y < 0 or y > 7):
                                    if not board[y][x] == None:
                                        if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "T": # Check if its the white king
                                            return True
                                else:
                                    break

                        # Bishop, Queen
                        if e_type == "B" or e_type == "Q":
                            directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
                            for direction in directions:
                                dx, dy = direction
                                x = indexX
                                y = indexY
                                while True:
                                    x += dx
                                    y += dy
                                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                                        if not board[y][x] == None:
                                            if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "T": # Check if its the white king
                                                return True
                                    else:
                                        break

                        # Knight
                        if e_type == "N":
                            moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
                            for move in moves:
                                dx, dy = move
                                x = indexX + dx
                                y = indexY + dx
                                if not (x < 0 or x > 7 or y < 0 or y > 7):
                                    if not board[y][x] == None:
                                        if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "T": # Check if its the white king
                                            return True

                        # Pawn
                        if e_type == "P":
                            x = indexX
                            y = indexY
                            moves = [(1, 1), (-1, 1)]
                            for move in moves:
                                dx, dy = move
                                x = indexX + dx
                                y = indexY + dy
                                if not (x < 0 or x > 7 or y < 0 or y > 7):
                                    if not board[y][x] == None:
                                        if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "T": # Check if its the white king
                                            return True
                        # King
                        if e_type == "K":
                            moves = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
                            for move in moves:
                                dx, dy = move
                                x = indexX + dx
                                y = indexY + dy
                                if not (x < 0 or x > 7 or y < 0 or y > 7):
                                    if not board[y][x] == None:
                                        if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "T": # Check if its the white king
                                            return True
                indexX += 1
            indexY += 1
    if atTurn == "Black": # Black has pullt. Now at turn is White
        for yFor in board:
            for e in yFor:
                if not e == None:
                    if list(e)[2] == "F": # Check if its a white figure
                        e_type = list(e)[0]
                        # Tower, Queen
                        if e_type == "T" or e_type == "Q":
                            x = indexX
                            y = indexY
                            while True:
                                x += 1
                                if not (x < 0 or x > 7 or y < 0 or y > 7):
                                    if not board[y][x] == None:
                                        if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "F": # Check if its the black king
                                            return True
                                else:
                                    break
                            x = indexX
                            y = indexY
                            while True:
                                x -= 1
                                if not (x < 0 or x > 7 or y < 0 or y > 7):
                                    if not board[y][x] == None:
                                        if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "F": # Check if its the black king
                                            return True
                                else:
                                    break
                            x = indexX
                            y = indexY
                            while True:
                                y += 1
                                if not (x < 0 or x > 7 or y < 0 or y > 7):
                                    if not board[y][x] == None:
                                        if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "F": # Check if its the black king
                                            return True
                                else:
                                    break
                            x = indexX
                            y = indexY
                            while True:
                                y -= 1
                                if not (x < 0 or x > 7 or y < 0 or y > 7):
                                    if not board[y][x] == None:
                                        if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "F": # Check if its the black king
                                            return True
                                else:
                                    break

                        # Bishop, Queen
                        if e_type == "B" or e_type == "Q":
                            directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
                            for direction in directions:
                                dx, dy = direction
                                x = indexX
                                y = indexY
                                while True:
                                    x += dx
                                    y += dy
                                    if not (x < 0 or x > 7 or y < 0 or y > 7):
                                        if not board[y][x] == None:
                                            if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "F": # Check if its the black king
                                                return True
                                    else:
                                        break

                        # Knight
                        if e_type == "N":
                            moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
                            for move in moves:
                                dx, dy = move
                                x = indexX + dx
                                y = indexY + dy
                                if not (x < 0 or x > 7 or y < 0 or y > 7):
                                    if not board[y][x] == None:
                                        if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "F": # Check if its the black king
                                            return True

                        # Pawn
                        if e_type == "P":
                            x = e.x
                            y = e.y
                            moves = [(1, 1), (-1, 1)]
                            for move in moves:
                                dx, dy = move
                                x = indexX + dx
                                y = indexY + dy
                                if not (x < 0 or x > 7 or y < 0 or y > 7):
                                    if not board[y][x] == None:
                                        if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "F": # Check if its the black king
                                            return True
                        # King
                        if e_type == "K":
                            moves = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
                            for move in moves:
                                dx, dy = move
                                x = indexX + dx
                                y = indexY + dy
                                if not (x < 0 or x > 7 or y < 0 or y > 7):
                                    if not board[y][x] == None:
                                        if list(board[y][x])[0] == "K" and list(board[y][x])[2] == "F": # Check if its the black king
                                            return True
                                    
def isCheck(turns: list, array: list, board: list, onTurn: str) -> list:
    i = 0
    for turn in turns:
        newBoard = move(turn, array, board, onTurn)
        if canTakeKing(newBoard, onTurn):
            turns.pop(i)
        i += 1
    return turns

def move(turn: list, array: list, board: list, onTurn: str) -> list:
    element = (turn[0]) - 1
    if onTurn == "White":
        id = array[0][element].id
    else:
        id = array[1][element].id
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == id:
                newx = turn[1]
                newy = turn[2]
                board[y][x] = None
                board[newy][newx] = id
    return board
