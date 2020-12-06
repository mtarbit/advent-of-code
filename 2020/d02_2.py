#!/usr/bin/env python3

from aoc import get_lines, get_input
import re


def is_valid(pw, ch, lo, hi):
    has_lo = (pw[lo - 1] == ch)
    has_hi = (pw[hi - 1] == ch)
    return has_lo ^ has_hi


def run(input):
    n = 0
    for s in input:
        lo, hi, ch, pw = re.match('(\d+)-(\d+) ([a-z]): ([a-z]+)', s).groups()
        lo, hi = int(lo), int(hi)
        if is_valid(pw, ch, lo, hi):
            n += 1
    return n


if __name__ == '__main__':
    assert run(get_lines('''
        1-3 a: abcde
        1-3 b: cdefg
        2-9 c: ccccccccc
    ''')) == 1
    print(run(get_input('d02')))
