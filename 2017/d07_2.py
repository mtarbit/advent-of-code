#!/usr/bin/env python

import re
import textwrap
from collections import Counter


def get_weight(key, res):
    weight = res[key]['weight']
    children = res[key]['children']

    if not children:
        return weight
    else:
        return weight + sum(get_weight(k, res) for k in children)


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
            'weight': int(weight),
        }

    for key, val in res.items():
        val['child_weights'] = [get_weight(k2, res) for k2 in val['children']]

    rebalanced = None
    unbalanced = None
    for key, val in res.items():
        counter = Counter(val['child_weights'])
        uniques = [x for x,n in counter.items() if n < 2]
        repeats = [x for x,n in counter.items() if n > 1]

        if len(uniques) == 1:
            unbalanced = val['children'][val['child_weights'].index(uniques[0])]
            rebalanced = res[unbalanced]['weight'] - (uniques[0] - repeats[0])
            if debug:
                print '-' * 80
                print 'unbalanced child:', unbalanced
                print 'rebalanced value:', rebalanced
                print 'parent:', key
                print 'parent data:', val

    return unbalanced, rebalanced


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
    """) == ('ugml', 60)

    with open('input/d07.txt') as f:
        print run(f.read(), debug=True)

