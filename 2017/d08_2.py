#!/usr/bin/env python

import collections
import textwrap


def run(s, debug=False):
    arr = s.splitlines()
    res = collections.defaultdict(int)

    largest_ever = 0

    for i, line in enumerate(arr):
        inst, cond = line.split('if')

        reg1, tok1, val1 = cond.split()
        reg2, tok2, val2 = inst.split()

        val1 = int(val1)
        val2 = int(val2)

        ops = {
            '>':   lambda a, b: a >  b,
            '<':   lambda a, b: a <  b,
            '>=':  lambda a, b: a >= b,
            '<=':  lambda a, b: a <= b,
            '==':  lambda a, b: a == b,
            '!=':  lambda a, b: a != b,
            'inc': lambda a, b: a +  b,
            'dec': lambda a, b: a -  b,
        }

        if ops[tok1](res[reg1], val1):
            res[reg2] = ops[tok2](res[reg2], val2)
            if res[reg2] > largest_ever:
                largest_ever = res[reg2]

    largest = max(res.values())

    return largest, largest_ever, dict(res)


if __name__ == '__main__':
    assert run(textwrap.dedent("""
    b inc 5 if a > 1
    a inc 1 if b < 5
    c dec -10 if a >= 1
    c inc -20 if c == 10
    """).strip()) == (1, 10, {'a': 1, 'b': 0, 'c': -10})

    with open('input/d08.txt') as f:
        print run(f.read())
