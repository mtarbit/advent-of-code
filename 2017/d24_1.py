#!/usr/bin/env python

import re
from textwrap import dedent
from collections import defaultdict


def bridge(root, data):
    a, b = root
    for pair in data:
        c, d = pair
        if a == c or a == d \
        or b == c or b == d:
            pass


def run(s, debug=False):
    data = re.findall('(\d+)/(\d+)', s)
    data = [map(int, pair) for pair in data]

    for pair in data:
        a, b = pair
        if a == 0 or b == 0:
            bridge(pair, data)

    return result


if __name__ == '__main__':
    assert run(dedent("""
    0/2
    2/2
    2/3
    3/4
    3/5
    0/1
    10/1
    9/10
    """).strip()) == 31

#     with open('input/d24.txt') as f:
#         print(run(f.read().strip(), debug=True))
