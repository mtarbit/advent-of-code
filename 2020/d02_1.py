#!/usr/bin/env python3

from aoc import get_lines
import re


def is_valid(pw, ch, lo, hi):
    n = 0
    for x in pw:
        if x == ch:
            n += 1
            if n > hi:
                return False
    if n < lo:
        return False
    return True


def run(input):
    n = 0
    for s in input:
        lo, hi, ch, pw = re.match('(\d+)-(\d+) ([a-z]): ([a-z]+)', s).groups()
        lo, hi = int(lo), int(hi)
        if is_valid(pw, ch, lo, hi):
            n += 1
    return n


def main():
    assert run(get_lines('d02.example')) == 2
    return run(get_lines('d02'))


if __name__ == '__main__':
    print(main())
