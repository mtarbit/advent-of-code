#!/usr/bin/env python

from __future__ import print_function
from collections import defaultdict


def assert_equal(a, b):
    if a != b:
        raise AssertionError("{!r} is not equal to {!r}".format(a, b))


def print_debug(grid, size, x1, y1):
    for y2 in range(-size, size + 1):
        for x2 in range(-size, size + 1):
            if y1 == y2 and x1 == (x2 + 1):
                end = '['
            elif y1 == y2 and x1 == x2:
                end = ']'
            else:
                end = ' '
            print(grid[(x2, y2)], end=end)
        print()
    print()


def run(s, steps, debug=False):
    grid = defaultdict(lambda: '.')

    arr = s.splitlines()
    off = len(arr) // 2
    for y, line in enumerate(arr):
        for x, char in enumerate(line):
            grid[((x - off), (y - off))] = char

    infected = 0
    x, y = 0, 0
    dir = 0

    for i in range(steps):
        if debug:
            print_debug(grid, 4, x, y)

        cur = grid[(x, y)]

        if cur == '#':
            dir = (dir + 90) % 360
        else:
            dir = (dir - 90) % 360

        if cur == '.':
            grid[(x, y)] = '#'
            infected += 1
        else:
            grid[(x, y)] = '.'

        if   dir ==   0: y -= 1
        elif dir ==  90: x += 1
        elif dir == 180: y += 1
        elif dir == 270: x -= 1

    return infected


if __name__ == '__main__':
    assert_equal(run('..#\n#..\n...',     7),    5)
    assert_equal(run('..#\n#..\n...',    70, debug=True),   41)
    assert_equal(run('..#\n#..\n...', 10000), 5587)

    with open('input/d22.txt') as f:
        print(run(f.read().strip(), 10000))
