#!/usr/bin/env python

from textwrap import dedent
from math import sqrt


def assert_equal(a, b):
    if a != b:
        raise AssertionError("{!r} is not equal to {!r}".format(a, b))


def text_to_grid(text):
    grid = []

    l = len(text)
    n = int(sqrt(l))
    for i in range(0, l, n):
        grid.append(list(text[i:i + n]))

    return grid


def grid_to_text(grid):
    return ''.join([''.join(line) for line in grid])


def grid_pretty_print(grid):
    for line in grid:
        print ' '.join(line)
    print


def grid_perms(grid):
    return [
        transform(grid,   0), transform(grid,   0, 'v'), transform(grid,   0, 'h'),
        transform(grid,  90), transform(grid,  90, 'v'), transform(grid,  90, 'h'),
        transform(grid, 180),
        transform(grid, 270),
    ]


def grid_canvas(n):
    grid = []
    for i in range(n):
        grid.append(list('.' * n))
    return grid


def transform(grid_a, deg=None, axis=None):
    grid_b = grid_a[:]
    grid_b = rotate(grid_b, deg)
    grid_b = mirror(grid_b, axis)
    return grid_b


def mirror(grid_a, axis):
    n = len(grid_a)
    grid_b = grid_canvas(n)

    for ra in range(n):
        for ca in range(n):
            rb, cb = ra, ca
            if axis == 'v':
                cb = (n - ca - 1)
            elif axis == 'h':
                rb = (n - ra - 1)
            grid_b[rb][cb] = grid_a[ra][ca]

    return grid_b


def rotate(grid_a, deg):
    n = len(grid_a)
    grid_b = grid_canvas(n)

    for ra in range(n):
        for ca in range(n):
            rb, cb = ra, ca
            if deg == 90:
                rb, cb = ca, (n - ra - 1)
            elif deg == 180:
                rb, cb = (n - ra - 1), (n - ca - 1)
            elif deg == 270:
                rb, cb = (n - ca - 1), ra
            grid_b[rb][cb] = grid_a[ra][ca]

    return grid_b


def expand(grid, rules):
    n = len(grid)

    if not n % 2:
        grid_list = explode(grid, n, 2)
    elif not n % 3:
        grid_list = explode(grid, n, 3)

    grid_list = map(grid_to_text, grid_list)
    grid_list = [rules[grid_text] for grid_text in grid_list]
    grid = implode(grid_list)

    return grid


def explode(grid, n, m):
    grid_list = []
    for r in range(0, n, m):
        for c in range(0, n, m):
            grid_list.append([line[c:c + m] for line in grid[r:r + m]])
    return grid_list


def implode(grid_list):
    # Ugh, this is pretty confusing. Not sure if it'd
    # make more sense if grid_list was a grid_grid or
    # something so it actually looked like this:

    # 0,0 0,1 | 0,2 0,3 | 0,4 0,5
    # 1,0 1,1 | 1,2 1,3 | 1,4 1,5
    # --------+---------+--------
    # 2,0 2,1 | 2,2 2,3 | 2,4 2,5
    # 3,0 3,1 | 3,2 3,3 | 3,4 3,5
    # --------+---------+--------
    # 4,0 4,1 | 4,2 4,3 | 4,4 4,5
    # 5,0 5,1 | 5,2 5,3 | 5,4 5,5

    n = len(grid_list)
    m = int(sqrt(n))
    o = len(grid_list[0])

    grid = []
    for i in range(0, n, m):
        for r in range(o):
            grid_line = []
            for j in range(m):
                grid_line.extend(grid_list[i + j][r])
            grid.append(grid_line)
    return grid


def run(s, steps, debug=False):
    rules = {}

    for line in s.splitlines():
        src, dst = line.split(' => ')
        src = text_to_grid(src.replace('/', ''))
        dst = text_to_grid(dst.replace('/', ''))
        for src_grid in grid_perms(src):
            src_text = grid_to_text(src_grid)
            rules[src_text] = dst

    grid = [
        ['.', '#', '.'],
        ['.', '.', '#'],
        ['#', '#', '#'],
    ]

    for i in range(steps):
        if debug:
            grid_pretty_print(grid)
        grid = expand(grid, rules)

    return grid_to_text(grid).count('#')


if __name__ == '__main__':
    assert_equal(text_to_grid('...#'), [['.', '.'], ['.', '#']])
    assert_equal(grid_to_text([['.', '.'], ['.', '#']]), '...#')
    assert_equal(mirror([['.', '.'], ['.', '#']], 'h'), [['.', '#'], ['.', '.']])
    assert_equal(mirror([['.', '.'], ['.', '#']], 'v'), [['.', '.'], ['#', '.']])
    assert_equal(rotate([['.', '.'], ['.', '#']],  90), [['.', '.'], ['#', '.']])
    assert_equal(rotate([['.', '.'], ['.', '#']], 180), [['#', '.'], ['.', '.']])
    assert_equal(rotate([['.', '.'], ['.', '#']], 270), [['.', '#'], ['.', '.']])
    assert_equal(explode([['#', '.', '.', '#'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['#', '.', '.', '#']], 4, 2),
                         [[['#', '.'], ['.', '.']], [['.', '#'], ['.', '.']], [['.', '.'], ['#', '.']], [['.', '.'], ['.', '#']]])
    assert_equal(implode([[['#', '.'], ['.', '.']], [['.', '#'], ['.', '.']], [['.', '.'], ['#', '.']], [['.', '.'], ['.', '#']]]),
                         [['#', '.', '.', '#'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['#', '.', '.', '#']])

    assert_equal(run(dedent("""
    ../.# => ##./#../...
    .#./..#/### => #..#/..../..../#..#
    """).strip(), 2), 12)

    with open('input/d21.txt') as f:
        print run(f.read().strip(), 18, debug=True)
