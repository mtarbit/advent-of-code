#!/usr/bin/env python

import re
from textwrap import dedent


def children(node_graph, node):
    node_visits = set()
    node_queue = [node]
    while node_queue:
        node = node_queue.pop(0)
        if node in node_visits:
            continue
        node_visits.add(node)
        node_queue.extend(set(node_graph[node]) - node_visits)
    return node_visits


def run(s, debug=False):
    conn = {}
    conn_groups = []

    for match in re.finditer(r'^(\d+) <-> ((?:\d+(?:, )?)+)$', s, re.M):
        prog = int(match.group(1))
        prog_pipes = map(int, match.group(2).split(', '))
        conn[prog] = prog_pipes

    for prog, prog_pipes in conn.items():
        seen = False
        for conn_group in conn_groups:
            if prog in conn_group:
                seen = True; break
        if not seen:
            conn_groups.append(children(conn, prog))

    return len(conn_groups)


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
    """).strip(), debug=True) == 2

    with open('input/d12.txt') as f:
        print run(f.read().strip())
