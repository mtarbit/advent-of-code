#!/usr/bin/env python3


from aoc import get_lines, get_input
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


if __name__ == '__main__':
    assert run(get_lines('''
        ..##.......
        #...#...#..
        .#....#..#.
        ..#.#...#.#
        .#...##..#.
        ..#.##.....
        .#.#.#....#
        .#........#
        #.##...#...
        #...##....#
        .#..#...#.#
    ''')) == 336
    print(run(get_input('d03')))

