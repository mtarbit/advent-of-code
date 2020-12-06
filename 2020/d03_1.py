#!/usr/bin/env python3

from aoc import get_lines, get_input


def run(input):
    n = 0

    r, c = 0, 0
    rows = len(input)
    cols = len(input[0])

    while r < (rows - 1):
        r = (r + 1)
        c = (c + 3) % cols
        if input[r][c] == '#':
            n += 1

    return n


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
    ''')) == 7
    print(run(get_input('d03')))
