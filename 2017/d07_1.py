#!/usr/bin/env python

import re
import textwrap


def get_count(key, res):
    children = res[key]['children']

    if not children:
        return 1
    else:
        return sum(get_count(k, res) for k in children)


def run(s, debug=False):
    arr = textwrap.dedent(s).strip().splitlines()
    res = {}

    for i, line in enumerate(arr):
        line_chunks = line.split(' -> ')
        key, weight = re.match(r'^(\w+) \((\d+)\)', line_chunks[0]).groups()

        if len(line_chunks) == 2:
            children = line_chunks[1].split(', ')
        else:
            children = []

        res[key] = {
            'children': children,
            'weight': weight,
            'n': 0,
        }

    for k, v in res.items():
        v['n'] = get_count(k, res)

    res = list(res.items())
    res = sorted(res, key=lambda x: x[1]['n'], reverse=True)

    if debug:
        print '\n'.join([repr((k, v)) for k, v in res])

    return res[0][0]


if __name__ == '__main__':
    assert run("""
    pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)
    """) == 'tknk'

    with open('input/d07.txt') as f:
        print run(f.read())

