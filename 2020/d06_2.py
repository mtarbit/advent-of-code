#!/usr/bin/env python3

from aoc import get_paras
from collections import defaultdict


def run(input):
    total = 0
    for group in input:
        lines = group.splitlines()
        yeses = defaultdict(int)
        group_size = len(lines)
        for line in lines:
            for char in line:
                yeses[char] += 1
        for char, count in yeses.items():
            if count == group_size:
                total += 1
    return total


def main():
    assert run(get_paras('d06.example')) == 6
    return run(get_paras('d06'))


if __name__ == '__main__':
    print(main())
