import os
from time import sleep
from random import random

[columns, rows] = os.get_terminal_size()


# create the matrix
def createMatrix():
    matrix = []
    for x in range(rows):
        col = []
        for y in range(columns):
            col.append("1" if random() > 0.9 else "0")
        matrix.append(col)
    return matrix


def isAlive(x, y, matrix):
    voisinsAlive = 0
    for row in range(-1, 2):
        for column in range(-1, 2):
            if row or column:
                if (
                    x + row >= 0
                    and x + row < rows
                    and y + column < columns
                    and y + column >= 0
                ):
                    if matrix[x + row][y + column] == "1":
                        voisinsAlive = voisinsAlive + 1
    return voisinsAlive == 2


def rebuildMatrix(matrix):
    newMatrix = []
    for i, col in enumerate(matrix):
        newCol = []
        for j, row in enumerate(col):
            newCol.append("1" if isAlive(i, j, matrix) else "0")
        newMatrix.append(newCol)
    return newMatrix


def printMatrix(matrix):
    for i, col in enumerate(matrix):
        for j, row in enumerate(col):
            print(matrix[i][j], end="")


def draw():
    temps = 0
    matrix = createMatrix()
    print(chr(27) + "[2J")  # clear screen
    while temps < 10:
        print(chr(27) + "[H")  # move to (0,0)
        # print(chr(27) + "[5;2f", end="")  # move to (5,2)
        printMatrix(matrix)
        matrix = rebuildMatrix(matrix)
        temps = temps + 1
        sleep(1)


draw()
