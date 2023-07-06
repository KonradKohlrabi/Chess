from canTakeKing import canTakeKing, getColor, isCheck, move

def calcPossibleTurns(array: list, atTurn: str, board: list) -> list:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
                            break

            # Knight

            if e_type == "N":
                x = e.x
                y = e.y
                y += 2
                x -= 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not getColor(y, x, board):
                        possibleTurns.append([i, x, y])

                x = e.x
                y = e.y
                y += 2
                x += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not getColor(y, x, board):
                        possibleTurns.append([i, x, y])

                x = e.x
                y = e.y
                y += 1
                x += 2
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not getColor(y, x, board):
                        possibleTurns.append([i, x, y])
                x = e.x
                y = e.y
                y = -1
                x += 2
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not getColor(y, x, board):
                        possibleTurns.append([i, x, y])

                x = e.x
                y = e.y
                y -= 2
                x += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not getColor(y, x, board):
                        possibleTurns.append([i, x, y])
                x = e.x
                y = e.y
                y -= 2
                x -= 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not getColor(y, x, board):
                        possibleTurns.append([i, x, y])

                x = e.x
                y = e.y
                y -= 1
                x -= 2
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not getColor(y, x, board):
                        possibleTurns.append([i, x, y])

                x = e.x
                y = e.y
                y += 1
                x -= 2
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not getColor(y, x, board):
                        possibleTurns.append([i, x, y])

            # Pawn

            if e_type == "P":
                x = e.x
                y = e.y
                y += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])

                if e.onBaseline:
                    y += 1
                    if x < 0 and x > 7 and y < 0 and y > 7:
                        pass
                    else:
                        if board[y][x] == None:
                            possibleTurns.append([i, x, y])
                # Taking
                x = e.x
                y = e.y
                y += 1
                x -= 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                x = e.x
                y = e.y
                y += 1
                x += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])

            # King
            

            if e_type == "K":
                x = e.x
                y = e.y
                y += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                
                x = e.x
                y = e.y
                x += 1
                y += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])

                x = e.x
                y = e.y
                x += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                
                x = e.x
                y = e.y
                y -= 1
                x += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])

                x = e.x
                y = e.y
                y -= 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                x = e.x
                y = e.y
                y -= 1
                x -= 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])

                x = e.x
                y = e.y
                x -= 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                x = e.x
                y = e.y
                y += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                x = e.x
                y = e.y
                y += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                x = e.x
                y = e.y
                y += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if not getColor(y, x, board):
                            possibleTurns.append([i, x, y])
            i += 1
    else:
        for e in array[1]:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
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
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                            break
                        else:
                            break

            # Knight

            if e_type == "N":
                x = e.x
                y = e.y
                y += 2
                x -= 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if getColor(y, x, board):
                        possibleTurns.append([i, x, y])

                x = e.x
                y = e.y
                y += 2
                x += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if getColor(y, x, board):
                        possibleTurns.append([i, x, y])

                x = e.x
                y = e.y
                y += 1
                x += 2
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if getColor(y, x, board):
                        possibleTurns.append([i, x, y])
                x = e.x
                y = e.y
                y = -1
                x += 2
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if getColor(y, x, board):
                        possibleTurns.append([i, x, y])

                x = e.x
                y = e.y
                y -= 2
                x += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if getColor(y, x, board):
                        possibleTurns.append([i, x, y])
                x = e.x
                y = e.y
                y -= 2
                x -= 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if getColor(y, x, board):
                        possibleTurns.append([i, x, y])

                x = e.x
                y = e.y
                y -= 1
                x -= 2
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if getColor(y, x, board):
                        possibleTurns.append([i, x, y])

                x = e.x
                y = e.y
                y += 1
                x -= 2
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if getColor(y, x, board):
                        possibleTurns.append([i, x, y])

            # Pawn

            if e_type == "P":
                x = e.x
                y = e.y
                y += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if board[y][x] == None:
                        possibleTurns.append([i, x, y])

                if e.onBaseline:
                    y += 1
                    if x < 0 and x > 7 and y < 0 and y > 7:
                        pass
                    else:
                        if board[y][x] == None:
                            possibleTurns.append([i, x, y])
                # Taking
                x = e.x
                y = e.y
                y += 1
                x -= 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                x = e.x
                y = e.y
                y += 1
                x += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])

            # King
            

            if e_type == "K":
                x = e.x
                y = e.y
                y += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                
                x = e.x
                y = e.y
                x += 1
                y += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])

                x = e.x
                y = e.y
                x += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                
                x = e.x
                y = e.y
                y -= 1
                x += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])

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
                    if not board[y][x] == None:
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                x = e.x
                y = e.y
                y += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                x = e.x
                y = e.y
                y += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
                x = e.x
                y = e.y
                y += 1
                if x < 0 and x > 7 and y < 0 and y > 7:
                    pass
                else:
                    if not board[y][x] == None:
                        if getColor(y, x, board):
                            possibleTurns.append([i, x, y])
            i += 1
    return possibleTurns
