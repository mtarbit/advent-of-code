#!/usr/bin/env python

import re
from textwrap import dedent


def connections(conn, seen, key):
    val = conn[key]
    if seen.issuperset(val):
        return 1
    else:
        seen.update(val)
        return sum(connections(conn, seen, k) for k in val)


def run(s):
    conn = {}

    for match in re.finditer(r'^(\d+) <-> ((?:\d+(?:, )?)+)$', s, re.M):
        prog = int(match.group(1))
        prog_pipes = map(int, match.group(2).split(', '))
        conn[prog] = prog_pipes

    return connections(conn, set([0]), 0)


if __name__ == '__main__':
    assert run(dedent("""
    0 <-> 2
    1 <-> 1, 7
    2 <-> 0, 3, 4
    3 <-> 2, 4
    4 <-> 2, 3, 6
    5 <-> 6
    6 <-> 4, 5
    7 <-> 1, 8, 9
    8 <-> 7
    9 <-> 7
    """).strip()) == 6

    with open('input/d12.txt') as f:
        print run(f.read().strip())
