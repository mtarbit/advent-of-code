#!/usr/bin/env python3


from aoc import get_lines
from functools import reduce
from operator import mul


def check_slope(input, dx, dy):
    n = 0

    x, y = 0, 0
    rows = len(input)
    cols = len(input[0])

    while y < (rows - dy):
        x = (x + dx) % cols
        y = (y + dy)
        if input[y][x] == '#':
            n += 1

    return n


def run(input):
    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )

    trees = []
    for dc, dr in slopes:
        trees.append(check_slope(input, dc, dr))

    return reduce(mul, trees)


def main():
    assert run(get_lines('d03.example')) == 336
    return run(get_lines('d03'))


if __name__ == '__main__':
    print(main())
