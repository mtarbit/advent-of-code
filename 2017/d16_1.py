#!/usr/bin/env python

from string import letters


def run(progs, moves, debug=False):
    progs = list(letters[:progs])
    moves = moves.split(',')

    for move in moves:
        move_type = move[0]
        move_args = move[1:]

        if move_type == 's':
            n = int(move_args)
            progs = progs[-n:] + progs[:-n]
        elif move_type == 'x':
            i, j = map(int, move_args.split('/'))
            progs[i], progs[j] = progs[j], progs[i]
        elif move_type == 'p':
            a, b = move_args.split('/')
            i, j = progs.index(a), progs.index(b)
            progs[i], progs[j] = progs[j], progs[i]

        if debug:
            print move, ':', ''.join(progs)

    return ''.join(progs)


if __name__ == '__main__':
    assert run(5, 's1,x3/4,pe/b', debug=True) == 'baedc'

    with open('input/d16.txt') as f:
        print run(16, f.read().strip())
