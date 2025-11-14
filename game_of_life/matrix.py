from random import random

type Matrix = list[list[bool]]


def create_matrix(rows=10, columns=10, alive_percent=30) -> Matrix:
    matrix = []
    for _row in range(rows):
        ligne = []
        for _colum in range(columns):
            ligne.append(random() < (alive_percent / 100))
        matrix.append(ligne)
    return matrix


def is_alive(x: int, y: int, matrix: Matrix) -> bool:
    """
    dead cell become alive if voisin ==3
    alive cell survive if voisin ==3 or voisin ==2
    """
    voisins_alive = 0
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
                        voisins_alive = voisins_alive + 1
    return voisins_alive == 3 or matrix[x][y] and voisins_alive == 2


def rebuild_matrix(matrix: Matrix) -> Matrix:
    new_matrix = []
    for i, row in enumerate(matrix):
        new_row = []
        for j, _column in enumerate(row):
            new_row.append(is_alive(i, j, matrix))
        new_matrix.append(new_row)
    return new_matrix


def print_matrix(matrix: Matrix, alive_char="\u2588", dead_char=" "):
    for i, col in enumerate(matrix):
        for j, _row in enumerate(col):
            print(alive_char if matrix[i][j] else dead_char, end="")
