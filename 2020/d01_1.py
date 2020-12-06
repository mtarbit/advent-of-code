#!/usr/bin/env python3

from aoc import get_input


def run(input):
    for i, n in enumerate(input):
        for m in input[(i + 1):]:
            if n + m == 2020:
                return n * m


if __name__ == '__main__':
    assert run([1721, 979, 366, 299, 675, 1456]) == 514579
    print(run(get_input('d01', int)))
