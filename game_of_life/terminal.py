import argparse
from game_of_life.main import main as game


def main():
    parser = argparse.ArgumentParser(
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

    game(alive_percent=args.percent, alive_char=args.alive)


if __name__ == "__main__":
    main()
