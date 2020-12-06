#!/usr/bin/env python

import re
import textwrap


class SparseList(list):
    def __setitem__(self, index, value):
        missing = index - len(self) + 1
        if missing > 0:
            self.extend([None] * missing)
        super(SparseList, self).__setitem__(index, value)

    def __getitem__(self, index):
        try:
            return super(SparseList, self).__getitem__(index)
        except IndexError:
            return None


# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 2 1 0 1 2 3 2 1 0 1 2 3
# -     -     -     -     -     -
# /     \     /     \     /     \


def state(i, r):
    r = r - 1
    d = r * 2
    j = i % d
    if j > r:
        j = d - j
    return j


def run(s, debug=False):
    layers = SparseList()
    severity = 0

    for match in re.finditer(r'^(\d+): (\d+)$', s, re.M):
        layer_depth = int(match.group(1))
        layer_range = int(match.group(2))
        layers[layer_depth] = layer_range

    for i, layer_range in enumerate(layers):
        if layer_range and state(i, layer_range) == 0:
            severity += (i * layer_range)

    return severity


if __name__ == '__main__':
    assert run(textwrap.dedent("""
    0: 3
    1: 2
    4: 4
    6: 4
    """).strip(), debug=True) == 24

    with open('input/d13.txt') as f:
        print run(f.read().strip())
