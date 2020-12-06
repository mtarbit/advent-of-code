#!/usr/bin/env python

import sys
from string import letters


class Move(object):
    def __init__(self, move):
        self.type = move[0]
        self.args = move[1:]

        if self.type == 's':
            self.n = int(self.args)
        elif self.type == 'x':
            i, j = map(int, self.args.split('/'))
            self.i = i
            self.j = j
        elif self.type == 'p':
            a, b = self.args.split('/')
            self.a = a
            self.b = b


def dance(progs, moves):
    for move in moves:
        if move.type == 's':
            n = move.n
            progs = progs[-n:] + progs[:-n]
        elif move.type == 'x':
            i, j = move.i, move.j
            progs[i], progs[j] = progs[j], progs[i]
        elif move.type == 'p':
            a, b = move.a, move.b
            i, j = progs.index(a), progs.index(b)
            progs[i], progs[j] = progs[j], progs[i]
    return progs


def run(progs, moves, times, debug=False):
    progs = list(letters[:progs])
    moves = [Move(m) for m in moves.split(',')]
    perms = []

    for i in xrange(times):
        progs = dance(progs, moves)
        joint = ''.join(progs)

        if joint in perms:
            index = (times % len(perms)) - 1
            short = perms[index]
            print "found a shortcut:", short
            return short

        perms.append(joint)

    print "finished looping:", joint

    return joint


if __name__ == '__main__':
    assert run(5, 's1,x3/4,pe/b', 2) == 'ceadb'

    with open('input/d16.txt') as f:
        print run(16, f.read().strip(), 10 ** 9, debug=True)
