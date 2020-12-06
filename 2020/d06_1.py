#!/usr/bin/env python3

from aoc import get_paras, get_input


def run(input):
    count = 0
    for group in input:
        lines = group.splitlines()
        yeses = set()
        for line in lines:
            yeses.update(set(line))
        count += len(yeses)
    return count


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
    ''')) == 11
    print(run(get_input('d06', lines=False, paras=True)))
