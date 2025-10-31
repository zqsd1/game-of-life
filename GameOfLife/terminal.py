import os
from time import sleep
from random import random

# [columns, rows] = os.get_terminal_size()
# alive = "\u2588"  # "#"
# dead = " "
alive = 1
dead = 0


def create_matrix(columns=10, rows=10):
    matrix = []
    for row in range(rows):
        ligne = []
        for colum in range(columns):
            ligne.append(alive if random() < 0.3 else dead)
        matrix.append(ligne)
    return matrix


def is_alive(x, y, matrix):
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
                    if matrix[x + row][y + column] == alive:
                        print(x + row, y + column)
                        voisinsAlive = voisinsAlive + 1
    return voisinsAlive == 3


def rebuild_matrix(matrix):
    newMatrix = []
    for i, row in enumerate(matrix):
        newRow = []
        for j, column in enumerate(row):
            newRow.append(alive if is_alive(i, j, matrix) else dead)
        newMatrix.append(newRow)
    return newMatrix


def print_matrix(matrix):
    for i, col in enumerate(matrix):
        for j, row in enumerate(col):
            print(matrix[i][j], end="")


def draw():
    temps = 0
    try:
        [columns, rows] = os.get_terminal_size()
    except Exception:
        [columns, rows] = [10, 10]
    matrix = create_matrix(rows=rows, columns=columns)
    print(chr(27) + "[2J")  # clear screen
    while temps < 30:
        print(chr(27) + "[H")  # move to (0,0)
        print_matrix(matrix)
        matrix = rebuild_matrix(matrix)
        temps = temps + 1
        sleep(1)


# draw()
matrix = [[0, 1, 0], [1, 1, 1], [0, 0, 1]]
is_alive(1, 1, matrix)
