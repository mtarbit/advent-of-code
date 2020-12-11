#!/usr/bin/env python3

from aoc import get_lines
from collections import defaultdict


def run(input):
    input = list(map(int, input))
    input.extend([0, max(input) + 3])
    input = sorted(input)
    diffs = defaultdict(int)

    for i in range(len(input) - 1):
        n = input[i]
        m = input[i + 1]
        diffs[m - n] += 1

    return diffs[1] * diffs[3]


def main():
    assert run(get_lines('d10.example.small')) == 35
    assert run(get_lines('d10.example.large')) == 220
    return run(get_lines('d10'))


if __name__ == '__main__':
    print(main())
