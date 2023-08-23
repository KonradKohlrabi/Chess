import pygame
import sys
import calcPossibleTurns
from classes import Bishop, King, Knight, Pawn, Queen, Tower

pygame.init()

screen = pygame.display.set_mode((400, 400))
colBlack = (139, 69, 19)
colWhite = (255,248,220)

players = [
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

board = [
    ["T1True", "N1True", "B1True", "Q1True", "K1True", "B2True", "N2True", "T2True"],
    ["P1True", "P2True", "P3True", "P4True", "P5True", "P6True", "P7True", "P8True"],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    ["P1False", "P2False", "P3False", "P4False", "P5False", "P6False", "P7False", "P8False"],
    ["T1False","N1False","B1False","Q1False","K1False","B2False","N2False","T2False"],
]

coordinates = [
    [(0, 0), (50, 0), (100, 0), (150, 0), (200, 0), (250, 0), (300, 0), (350, 0),],
    [(0, 50), (50, 50), (100, 50), (150, 50), (200, 50), (250, 50), (300, 50), (350, 50),],
    [(0, 100), (50, 100), (100, 100), (150, 100), (200, 100), (250, 100), (300, 100), (350, 100),],
    [(0, 150), (50, 150), (100, 150), (150, 150), (200, 150), (250, 150), (300, 150), (350, 150),],
    [(0, 200), (50, 200), (100, 200), (150, 200), (200, 200), (250, 200), (300, 200), (350, 200),],
    [(0, 250), (50, 250), (100, 250), (150, 250), (200, 250), (250, 250), (300, 250), (350, 250),],
    [(0, 300), (50, 300), (100, 300), (150, 300), (200, 300), (250, 300), (300, 300), (350, 300),],
    [(0, 350), (50, 350), (100, 350), (150, 350), (200, 350), (250, 350), (300, 350), (350, 350),],
]

def printBoard(coordinates):
    bishopWhite = pygame.image.load("img/White/Bishop.png")
    kingWhite = pygame.image.load("img/White/King.png")
    knightWhite = pygame.image.load("img/White/Knight.png")
    pawnWhite = pygame.image.load("img/White/Pawn.png")
    queenWhite = pygame.image.load("img/White/Queen.png")
    towerWhite = pygame.image.load("img/White/Tower.png")
    bishopBlack = pygame.image.load("img/Black/Bishop.png")
    kingBlack = pygame.image.load("img/Black/King.png")
    knightBlack = pygame.image.load("img/Black/Knight.png")
    pawnBlack = pygame.image.load("img/Black/Pawn.png")
    queenBlack = pygame.image.load("img/Black/Queen.png")
    towerBlack = pygame.image.load("img/Black/Tower.png")

    bishopWhite = pygame.transform.scale(bishopWhite, (50, 50))
    kingWhite = pygame.transform.scale(kingWhite, (50, 50))
    knightWhite = pygame.transform.scale(knightWhite, (50, 50))
    pawnWhite = pygame.transform.scale(pawnWhite, (50, 50))
    queenWhite = pygame.transform.scale(queenWhite, (50, 50))
    towerWhite = pygame.transform.scale(towerWhite, (50, 50))
    bishopBlack = pygame.transform.scale(bishopBlack, (50, 50))
    kingBlack = pygame.transform.scale(kingBlack, (50, 50))
    knightBlack = pygame.transform.scale(knightBlack, (50, 50))
    pawnBlack = pygame.transform.scale(pawnBlack, (50, 50))
    queenBlack = pygame.transform.scale(queenBlack, (50, 50))
    towerBlack = pygame.transform.scale(towerBlack, (50, 50))
    iy = 0
    for y in board:
        ix = 0
        for x in y:
            if not (x == None):
                figure_type = list(x)[0]
                figure_color = list(x)[2]
                insertion_point = coordinates[iy][ix]
                if figure_color == "T": # White
                    if figure_type == "T":
                        screen.blit(towerWhite, insertion_point)
                    elif figure_type == "N":
                        screen.blit(knightWhite, insertion_point)
                    elif figure_type == "B":
                        screen.blit(bishopWhite, insertion_point)
                    elif figure_type == "Q":
                        screen.blit(queenWhite, insertion_point)
                    elif figure_type == "K":
                        screen.blit(kingWhite, insertion_point)
                    elif figure_type == "P":
                        screen.blit(pawnWhite, insertion_point)
                else: # Black
                    if figure_type == "T":
                        screen.blit(towerBlack, insertion_point)
                    elif figure_type == "N":
                        screen.blit(knightBlack, insertion_point)
                    elif figure_type == "B":
                        screen.blit(bishopBlack, insertion_point)
                    elif figure_type == "Q":
                        screen.blit(queenBlack, insertion_point)
                    elif figure_type == "K":
                        screen.blit(kingBlack, insertion_point)
                    elif figure_type == "P":
                        screen.blit(pawnBlack, insertion_point)
            ix += 1
        iy += 1

def drawBackground():
    # Raw 1
    pygame.draw.rect(screen, colWhite, (0, 0, 50, 50))
    pygame.draw.rect(screen, colWhite, (100, 0, 50, 50))
    pygame.draw.rect(screen, colWhite, (200, 0, 50, 50))
    pygame.draw.rect(screen, colWhite, (300, 0, 50, 50))

    pygame.draw.rect(screen, colBlack, (50, 0, 50, 50))
    pygame.draw.rect(screen, colBlack, (150, 0, 50, 50))
    pygame.draw.rect(screen, colBlack, (250, 0, 50, 50))
    pygame.draw.rect(screen, colBlack, (350, 0, 50, 50))


    # Raw 2
    pygame.draw.rect(screen, colWhite, (50, 50, 50, 50))
    pygame.draw.rect(screen, colWhite, (150, 50, 50, 50))
    pygame.draw.rect(screen, colWhite, (250, 50, 50, 50))
    pygame.draw.rect(screen, colWhite, (350, 50, 50, 50))

    pygame.draw.rect(screen, colBlack, (0, 50, 50, 50))
    pygame.draw.rect(screen, colBlack, (100, 50, 50, 50))
    pygame.draw.rect(screen, colBlack, (200, 50, 50, 50))
    pygame.draw.rect(screen, colBlack, (300, 50, 50, 50))


    # Raw 3
    pygame.draw.rect(screen, colWhite, (0, 100, 50, 50))
    pygame.draw.rect(screen, colWhite, (100, 100, 50, 50))
    pygame.draw.rect(screen, colWhite, (200, 100, 50, 50))
    pygame.draw.rect(screen, colWhite, (300, 100, 50, 50))

    pygame.draw.rect(screen, colBlack, (50, 100, 50, 50))
    pygame.draw.rect(screen, colBlack, (150, 100, 50, 50))
    pygame.draw.rect(screen, colBlack, (250, 100, 50, 50))
    pygame.draw.rect(screen, colBlack, (350, 100, 50, 50))


    # Raw 4
    pygame.draw.rect(screen, colWhite, (50, 150, 50, 50))
    pygame.draw.rect(screen, colWhite, (150, 150, 50, 50))
    pygame.draw.rect(screen, colWhite, (250, 150, 50, 50))
    pygame.draw.rect(screen, colWhite, (350, 150, 50, 50))

    pygame.draw.rect(screen, colBlack, (0, 150, 50, 50))
    pygame.draw.rect(screen, colBlack, (100, 150, 50, 50))
    pygame.draw.rect(screen, colBlack, (200, 150, 50, 50))
    pygame.draw.rect(screen, colBlack, (300, 150, 50, 50))


    # Raw 5
    pygame.draw.rect(screen, colWhite, (0, 200, 50, 50))
    pygame.draw.rect(screen, colWhite, (100, 200, 50, 50))
    pygame.draw.rect(screen, colWhite, (200, 200, 50, 50))
    pygame.draw.rect(screen, colWhite, (300, 200, 50, 50))

    pygame.draw.rect(screen, colBlack, (50, 200, 50, 50))
    pygame.draw.rect(screen, colBlack, (150, 200, 50, 50))
    pygame.draw.rect(screen, colBlack, (250, 200, 50, 50))
    pygame.draw.rect(screen, colBlack, (350, 200, 50, 50))


    # Raw 6
    pygame.draw.rect(screen, colWhite, (50, 250, 50, 50))
    pygame.draw.rect(screen, colWhite, (150, 250, 50, 50))
    pygame.draw.rect(screen, colWhite, (250, 250, 50, 50))
    pygame.draw.rect(screen, colWhite, (350, 250, 50, 50))

    pygame.draw.rect(screen, colBlack, (0, 250, 50, 50))
    pygame.draw.rect(screen, colBlack, (100, 250, 50, 50))
    pygame.draw.rect(screen, colBlack, (200, 250, 50, 50))
    pygame.draw.rect(screen, colBlack, (300, 250, 50, 50))


    # Raw 7
    pygame.draw.rect(screen, colWhite, (0, 300, 50, 50))
    pygame.draw.rect(screen, colWhite, (100, 300, 50, 50))
    pygame.draw.rect(screen, colWhite, (200, 300, 50, 50))
    pygame.draw.rect(screen, colWhite, (300, 300, 50, 50))

    pygame.draw.rect(screen, colBlack, (50, 300, 50, 50))
    pygame.draw.rect(screen, colBlack, (150, 300, 50, 50))
    pygame.draw.rect(screen, colBlack, (250, 300, 50, 50))
    pygame.draw.rect(screen, colBlack, (350, 300, 50, 50))


    # Raw 8
    pygame.draw.rect(screen, colWhite, (50, 350, 50, 50))
    pygame.draw.rect(screen, colWhite, (150, 350, 50, 50))
    pygame.draw.rect(screen, colWhite, (250, 350, 50, 50))
    pygame.draw.rect(screen, colWhite, (350, 350, 50, 50))

    pygame.draw.rect(screen, colBlack, (0, 350, 50, 50))
    pygame.draw.rect(screen, colBlack, (100, 350, 50, 50))
    pygame.draw.rect(screen, colBlack, (200, 350, 50, 50))
    pygame.draw.rect(screen, colBlack, (300, 350, 50, 50))

    pygame.display.update()
drawBackground()
printBoard(coordinates)
pygame.display.update()

def showPossibleTurns(board, coordinate, array):
    x, y = coordinate
    id = board[y][x]
    color = None
    if list(id)[2] == "T":
        color = "White"
    else:
        color = "Black"
    allPossibleTurns = calcPossibleTurns.calcPossibleTurns(array, color, board)
    possibleTurns = []
    for i in allPossibleTurns:
        if i[3] == id:
            possibleTurns.append(i)
    return possibleTurns



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        leftBTN, middleBTN, rightBTN = pygame.mouse.get_pressed()
        if leftBTN == True:
            x, y = event.pos
            