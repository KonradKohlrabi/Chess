def canTakeKing(board: list, onTurn: str):
    for y in board:
        for e in y:
            if e == None:
                break
            e_color = list(e)[3]
            if e_color == "T" and onTurn == "White":
                e_type = list(e)[1]
                if e_type == "T":
                    x = e.x
                    y = e.y
                    while True:
                        x += 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][e] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                if e_type == "T":
                    x = e.x
                    y = e.y
                    while True:
                        y += 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][e] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                if e_type == "T":
                    x = e.x
                    y = e.y
                    while True:
                        x -= 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][e] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                if e_type == "T":
                    x = e.x
                    y = e.y
                    while True:
                        y -= 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][e] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                            
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
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                if e_type == "B":
                    x = e.x
                    y = e.y
                    while True:
                        x -= 1
                        y += 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][x] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                if e_type == "B":
                    x = e.x
                    y = e.y
                    while True:
                        x += 1
                        y -= 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][x] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                if e_type == "B":
                    x = e.x
                    y = e.y
                    while True:
                        x -= 1
                        y -= 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][x] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                            
                # Queen

                if e_type == "Q":
                    x = e.x
                    y = e.y
                    while True:
                        x -= 1
                        y -= 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][x] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                    x = e.x
                    y = e.y
                    while True:
                        x += 1
                        y -= 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][x] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                    x = e.x
                    y = e.y
                    while True:
                        x -= 1
                        y += 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][x] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                    x = e.x
                    y = e.y
                    while True:
                        x += 1
                        y += 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][x] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                    x = e.x
                    y = e.y
                    while True:
                        y -= 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][e] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                    x = e.x
                    y = e.y
                    while True:
                        x -= 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][e] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                    x = e.x
                    y = e.y
                    while True:
                        y += 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][e] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                    x = e.x
                    y = e.y
                    while True:
                        x += 1
                        if x == -1 or y == -1 or x == 8 or y == 8:
                            break
                        if board[y][e] == None:
                            pass
                        else:
                            if list(board[y][x])[0] == "K":
                                return True
                
                # Knight
                
                if e_type == "N":
                    x = e.x
                    y = e.y
                    y += 2
                    x -= 1
                    if list(board[y][x])[0] == "K":
                        return True
                    x = e.x
                    y = e.y
                    y += 2
                    x += 1
                    if list(board[y][x])[0] == "K":
                        return True
                    x = e.x
                    y = e.y
                    y += 1
                    x += 2
                    if list(board[y][x])[0] == "K":
                        return True
                    x = e.x
                    y = e.y
                    y = -1
                    x += 2
                    if list(board[y][x])[0] == "K":
                        return True

                    x = e.x
                    y = e.y
                    y -= 2
                    x += 1
                    if list(board[y][x])[0] == "K":
                        return True
                    x = e.x
                    y = e.y
                    y -= 2
                    x -= 1
                    if list(board[y][x])[0] == "K":
                        return True

                    x = e.x
                    y = e.y
                    y -= 1
                    x -= 2
                    if list(board[y][x])[0] == "K":
                        return True
                    x = e.x
                    y = e.y
                    y += 1
                    x -= 2
                    if list(board[y][x])[0] == "K":
                        return True
                
                # Pawn
                
                if e_type == "P":
                    x = e.x
                    y = e.y
                    y += 1
                    x -= 1
                    if x < 0 and x > 7 and y < 0 and y > 7:
                        pass
                    else:
                        if not board[y][x] == None:
                            if list(board[y][x])[0] == "K":
                                return True
                    x = e.x
                    y = e.y
                    y += 1
                    x += 1
                    if x < 0 and x > 7 and y < 0 and y > 7:
                        pass
                    else:
                        if not board[y][x] == None:
                            if list(board[y][x])[0] == "K":
                                return True
                    # King
            
                if e_type == "K":
                    x = e.x
                    y = e.y
                    y += 1
                    if x < 0 and x > 7 and y < 0 and y > 7:
                        pass
                    else:
                        if list(board[y][x])[0] == "K":
                            return True
                    
                    x = e.x
                    y = e.y
                    x += 1
                    y += 1
                    if x < 0 and x > 7 and y < 0 and y > 7:
                        pass
                    else:
                        if list(board[y][x])[0] == "K":
                            return True

                    x = e.x
                    y = e.y
                    x += 1
                    if x < 0 and x > 7 and y < 0 and y > 7:
                        pass
                    else:
                        if list(board[y][x])[0] == "K":
                            return True
                    
                    x = e.x
                    y = e.y
                    y -= 1
                    x += 1
                    if x < 0 and x > 7 and y < 0 and y > 7:
                        pass
                    else:
                        if list(board[y][x])[0] == "K":
                            return True

                    x = e.x
                    y = e.y
                    y -= 1
                    if x < 0 and x > 7 and y < 0 and y > 7:
                        pass
                    else:
                        if list(board[y][x])[0] == "K":
                            return True
                    x = e.x
                    y = e.y
                    y -= 1
                    x -= 1
                    if x < 0 and x > 7 and y < 0 and y > 7:
                        pass
                    else:
                        if list(board[y][x])[0] == "K":
                            return True

                    x = e.x
                    y = e.y
                    x -= 1
                    if x < 0 and x > 7 and y < 0 and y > 7:
                        pass
                    else:
                        if list(board[y][x])[0] == "K":
                            return True
                    x = e.x
                    y = e.y
                    y += 1
                    if x < 0 and x > 7 and y < 0 and y > 7:
                        pass
                    else:
                        if list(board[y][x])[0] == "K":
                            return True
                    x = e.x
                    y = e.y
                    y += 1
                    if x < 0 and x > 7 and y < 0 and y > 7:
                        pass
                    else:
                        if list(board[y][x])[0] == "K":
                            return True
                    x = e.x
                    y = e.y
                    y += 1
                    if x < 0 and x > 7 and y < 0 and y > 7:
                        pass
                    else:
                        if list(board[y][x])[0] == "K":
                            return True
    return False


def isCheck(turns: list, color: str, array: list, board: list, onTurn: str):
    i = 0
    for turn in turns:
        newBoard = move(turn, array, board)
        if canTakeKing(newBoard, onTurn):
            turns.pop(i)
        i += 1

def move(turn: list, array: list, board: list) -> list:
    id = array[turn][0].id
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == id:
                newx = x + turn[1]
                newy = y + turn[2]
                board[y][x] = None
                board[newy][newx] = id
                
        
def getColor(y: int, x: int, board: list) -> bool:
    e = board[y][x]
    if e == None:
        return False
    color = list(board[y][x])[2]
    if color == "T":
        return True # White
    else:
        return False # Black