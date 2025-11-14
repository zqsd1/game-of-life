import os
from time import sleep
from game_of_life.matrix import create_matrix, rebuild_matrix, print_matrix


def main():
    try:
        [columns, rows] = os.get_terminal_size()
    except Exception:
        [columns, rows] = [10, 10]

    matrix = create_matrix(rows=rows, columns=columns, alive_percent=25)
    print(chr(27) + "[2J")  # clear screen
    try:
        while True:
            print(chr(27) + "[H")  # move to (0,0)
            print_matrix(matrix, alive_char="#")
            matrix = rebuild_matrix(matrix)
            sleep(0.5)
    except Exception:
        pass


if __name__ == "__main__":
    main()
