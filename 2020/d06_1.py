#!/usr/bin/env python3

from aoc import get_paras


def run(input):
    count = 0
    for group in input:
        lines = group.splitlines()
        yeses = set()
        for line in lines:
            yeses.update(set(line))
        count += len(yeses)
    return count


def main():
    assert run(get_paras('d06.example')) == 11
    return run(get_paras('d06'))


if __name__ == '__main__':
    print(main())
