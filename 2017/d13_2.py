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


def layer_state(i, r):
    """
    Return a number from the zig-zagging
    sequence with period `p` as follows:
    ------------------------------------
    Index: 0 1 2 3 4 5 6 7 8 9
    Value: 0 1 2 3 2 1 0 1 2 3
    """
    r = r - 1
    p = r * 2
    n = i % p
    if n > r:
        n = p - n
    return n


def run(s, debug=False):
    layers = SparseList()

    for match in re.finditer(r'^(\d+): (\d+)$', s, re.M):
        layer_depth = int(match.group(1))
        layer_range = int(match.group(2))
        layers[layer_depth] = layer_range

    delay = 0
    while True:
        caught = False
        for i, layer_range in enumerate(layers):
            if layer_range and layer_state(delay + i, layer_range) == 0:
                caught = True; break
        if not caught:
            break
        delay += 1

    return delay


if __name__ == '__main__':
    assert run(textwrap.dedent("""
    0: 3
    1: 2
    4: 4
    6: 4
    """).strip(), debug=True) == 10

    with open('input/d13.txt') as f:
        print run(f.read().strip())
