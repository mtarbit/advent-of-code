#!/usr/bin/env python3

from aoc import get_lines


def run(input):
    input = list(map(int, input))
    for i, n in enumerate(input):
        for m in input[(i + 1):]:
            if n + m == 2020:
                return n * m


def main():
    assert run(get_lines('d01.example')) == 514579
    return run(get_lines('d01'))


if __name__ == '__main__':
    print(main())
