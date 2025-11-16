import argparse
import os
from game_of_life.matrix import create_matrix, print_matrix, rebuild_matrix
from time import sleep


def main():
    parser = argparse.ArgumentParser(
        prog="gol",
        description="play the game of life insde the terminal",
    )

    parser.add_argument(
        "-a", "--alive", help="the char used to represent alive cell", default="#"
    )
    parser.add_argument(
        "-p",
        "--percent",
        help="the percentage of alive cell at the start",
        type=int,
        default=25,
    )

    args = parser.parse_args()

    [columns, rows] = os.get_terminal_size()

    matrix = create_matrix(rows=rows, columns=columns, alive_percent=args.percent)
    print(chr(27) + "[2J")  # clear screen

    while True:
        print(chr(27) + "[H")  # move to (0,0)
        print_matrix(matrix, alive_char=args.alive)
        matrix = rebuild_matrix(matrix)
        sleep(0.5)


if __name__ == "__main__":
    main()
