import os
from time import sleep
from random import random

# [columns, rows] = os.get_terminal_size()
# alive = "\u2588"  # "#"
# dead = " "


def create_matrix(rows=10, columns=10, alive_percent=30):
    matrix = []
    for row in range(rows):
        ligne = []
        for colum in range(columns):
            ligne.append(random() < (alive_percent / 100))
        matrix.append(ligne)
    return matrix


def is_alive(x, y, matrix):
    """
    dead cell become alive if voisin ==3
    alive cell survive if voisin ==3 or voisin ==2
    """
    voisinsAlive = 0
    for row in (-1, 0, 1):
        for column in range(-1, 2):
            if row or column:
                if (
                    x + row >= 0
                    and x + row < len(matrix)
                    and y + column < len(matrix[row])
                    and y + column >= 0
                ):
                    if matrix[x + row][y + column]:
                        voisinsAlive = voisinsAlive + 1
    return voisinsAlive == 3 or matrix[x][y] and voisinsAlive == 2


def rebuild_matrix(matrix):
    newMatrix = []
    for i, row in enumerate(matrix):
        newRow = []
        for j, column in enumerate(row):
            newRow.append(is_alive(i, j, matrix))
        newMatrix.append(newRow)
    return newMatrix


def print_matrix(matrix, alive_char="\u2588", dead_char=" "):
    for i, col in enumerate(matrix):
        for j, row in enumerate(col):
            print(alive_char if matrix[i][j] else dead_char, end="")


def draw():
    temps = 0
    try:
        [columns, rows] = os.get_terminal_size()
    except Exception:
        [columns, rows] = [10, 10]
    matrix = create_matrix(rows=rows, columns=columns, alive_percent=10)
    print(chr(27) + "[2J")  # clear screen
    while temps < 30:
        print(chr(27) + "[H")  # move to (0,0)
        print_matrix(matrix, alive_char="#")
        matrix = rebuild_matrix(matrix)
        temps = temps + 1
        sleep(1)


draw()
