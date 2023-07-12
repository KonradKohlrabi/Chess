def canTakeKing(board: list, onTurn: str):
    pass


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