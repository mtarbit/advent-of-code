#!/usr/bin/env python3

from aoc import get_paras, get_input
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


if __name__ == '__main__':
    assert run(get_paras('''
        abc

        a
        b
        c

        ab
        ac

        a
        a
        a
        a

        b
    ''')) == 6
    print(run(get_input('d06', lines=False, paras=True)))
