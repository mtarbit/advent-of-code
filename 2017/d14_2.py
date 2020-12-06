#!/usr/bin/env python

from operator import xor


def sparse_hash_round(i, skip, nums, lengths):
    size = len(nums)

    for l in lengths:
        j = i + l
        k = (j % size) if j >= size else 0

        a = nums[i:j]
        b = nums[0:k]
        c = list(reversed(a + b))
        nums[i:j] = c[:len(a)]
        nums[0:k] = c[len(a):]

        i = (j + skip) % size

        skip += 1

    return i, skip, nums


def sparse_hash(lengths, rounds=64, size=256):
    i = 0
    skip = 0
    nums = list(range(size))
    lengths += [17, 31, 73, 47, 23]
    for round in range(rounds):
        i, skip, nums = sparse_hash_round(i, skip, nums, lengths)
    return nums


def dense_hash(nums, size):
    for i in range(0, len(nums), size):
        j = i + size
        yield reduce(xor, nums[i:j])


def knot_hash(s):
    lengths = map(ord, s)
    nums = sparse_hash(lengths)
    nums = dense_hash(nums, 16)
    bits = ['{:08b}'.format(n) for n in nums]
    return ''.join(bits)


CELL_ADJACENT = ((-1, 0), (0, -1), (0, 1), (1, 0))


def get_cell(grid, r, c):
    if r < 0 or c < 0:
        return
    try:
        return grid[r][c]
    except IndexError:
        return None


def set_cell(grid, r, c, n):
    if r < 0 or c < 0:
        return
    try:
        grid[r][c] = n
    except IndexError:
        pass


def flood_fill(grid, r, c, n):
    if get_cell(grid, r, c) != '#':
        return False
    set_cell(grid, r, c, n)
    for dr, dc in CELL_ADJACENT:
        flood_fill(grid, r + dr, c + dc, n)
    return True


def run(key, debug=False):
    grid = []

    for i in range(128):
        line = knot_hash('{}-{}'.format(key, i))
        grid.append(['#' if int(n) else '.' for n in line])

    n = 1
    for r, _ in enumerate(grid):
        for c, _ in enumerate(grid[r]):
            if flood_fill(grid, r, c, n):
                n += 1

    if debug:
        for line in grid[:8]:
            print line[:8]

    return (n - 1)


if __name__ == '__main__':
    assert run('flqrgnkx') == 1242

    with open('input/d14.txt') as f:
        print run(f.read().strip())
