#!/usr/bin/env python

import re
from textwrap import dedent
from collections import defaultdict


def run(s, debug=False):
    reg = defaultdict(int)
    arr = re.findall(r'^(\w+) (\w+) ?([\w-]+)?$', s, re.M)
    idx = 0

    def val(key):
        if key in reg:
            return reg.get(key)
        else:
            return int(key)

    stored = None

    while True:
        try:
            cmd, x, y = arr[idx]
        except IndexError:
            break

        if debug:
            print '{:>3d} {} {} {:6s} {}'.format(idx, cmd, x, y, dict(reg))

        if cmd == 'snd':
            stored = reg[x]
        elif cmd == 'set':
            reg[x] = val(y)
        elif cmd == 'add':
            reg[x] += val(y)
        elif cmd == 'mul':
            reg[x] *= val(y)
        elif cmd == 'mod':
            reg[x] %= val(y)
        elif cmd == 'rcv' and val(x) != 0:
            reg[x] = stored; return stored
        elif cmd == 'jgz' and val(x) > 0:
            idx += (val(y) - 1)

        idx += 1



if __name__ == '__main__':
    assert run(dedent("""
    set a 1
    add a 2
    mul a a
    mod a 5
    snd a
    set a 0
    rcv a
    jgz a -1
    set a 1
    jgz a -2
    """).strip()) == 4

    with open('input/d18.txt') as f:
        print run(f.read().strip(), debug=True)
