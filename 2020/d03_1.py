#!/usr/bin/env python3

from aoc import get_lines


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


def main():
    assert run(get_lines('d03.example')) == 7
    return run(get_lines('d03'))


if __name__ == '__main__':
    print(main())
