#!/usr/bin/env python

from textwrap import dedent
from string import letters


def assert_equal(a, b):
    if a != b:
        raise AssertionError("{!r} is not equal to {!r}".format(a, b))


def get_pos(grid, r, c):
    try:
        return grid[r][c]
    except IndexError:
        return '.'


def get_dir_h(grid, r, c, dir):
    if get_pos(grid, r, c - 1) != '.':
        return 'l'
    if get_pos(grid, r, c + 1) != '.':
        return 'r'


def get_dir_v(grid, r, c, dir):
    if get_pos(grid, r - 1, c) != '.':
        return 'u'
    if get_pos(grid, r + 1, c) != '.':
        return 'd'


def run(s, debug=False):
    path = []
    grid = s.splitlines()

    dir = 'd'
    pos = '|'

    r = 0
    c = grid[r].index(pos)

    steps = 1

    while True:
        if dir == 'u': r -= 1
        if dir == 'd': r += 1
        if dir == 'l': c -= 1
        if dir == 'r': c += 1

        pos = get_pos(grid, r, c)

        if pos in letters:
            path.append(pos)
        elif pos == '+' and dir in 'ud':
            dir = get_dir_h(grid, r, c, dir)
        elif pos == '+' and dir in 'lr':
            dir = get_dir_v(grid, r, c, dir)
        elif pos == '.':
            break

        steps += 1

        if debug:
            print steps, r, c, pos, dir, path

    return steps


if __name__ == '__main__':
    assert_equal(run(dedent("""
    .....|..........
    .....|..+--+....
    .....A..|..C....
    .F---|----E|--+.
    .....|..|..|..D.
    .....+B-+..+--+.
    ................
    """).strip()), 38)

    with open('input/d19.txt') as f:
        print run(f.read().strip())
