import os
from time import sleep

print(os.get_terminal_size())


def draw():
    temps = 0
    while temps < 10:
        print(chr(27) + "[2J")  # clear screen
        print(chr(27) + "[H")  # move to (0,0)
        print(f"le nombre est {temps}")
        temps = temps + 1
        sleep(1)


draw()
