#!/usr/bin/env python

from __future__ import print_function
import re
from textwrap import dedent
from collections import defaultdict
from math import sqrt


def asm():
    a = b = c = d = e = f = g = h = 0

    a = 1
    b = 81 # 1
    c = b  # 2

    if a == 0: # 3
        pass # 4
    else:
        b *= 100 # 5
        b += 100000 # 6
        c = b # 7
        c += 17000 # 8

    while True:
        f = 1 # 9
        d = 2 # 10

        while g: # 24
            e = 2 # 11

            while g: # 20
                g = d # 12
                g *= e # 13
                g -= b # 14

                if g == 0: # 15
                    f = 0 # 16

                e += 1 # 17
                g -= b # 19

                print('a:{} b:{} c:{} d:{} e:{} f:{} g:{} h:{}'.format(
                       a, b, c, d, e, f, g, h))

            d += 1 # 21
            g = d # 22
            g -= b # 23

        if f == 0: # 25
            h += 1 # 26

        g = b # 27
        g -= c # 28

        if g != 0:
            b += 17
        else:
            break


def asm_opt():
    a = 108100
    b = 125100

    result = 1
    primes = sieve(b)

    for n in xrange(a, b, 17):
        if not primes[n]: # is_composite(n): # 25
            print('.', end='')
            result += 1 # 26

    print()
    print(result)


def sieve(n):
    arr = [True] * (n + 1)

    for i in xrange(2, int(sqrt(n))):
        if arr[i]:
            for k in xrange(n):
                j = (i ** 2) + (i * k)
                if j > n: break
                arr[j] = False

    return arr


def is_composite(n):
    for a in xrange(2, n) : # 10, 21-24
        for b in xrange(2, n): # 11, 17-20
            if a * b == n: # 12-15
                return True
    return False


def run(s, debug=False):
    reg = defaultdict(int)
    arr = re.findall(r'^(\w+) (\w+) ?([\w-]+)?$', s, re.M)
    idx = 0

    def val(key):
        if key.isalpha():
            return reg[key]
        else:
            return int(key)

    stored = None
    result = 0

    reg['a'] = 1

    while True:
        try:
            cmd, x, y = arr[idx]
        except IndexError:
            break

        if debug:
            print('{:>3d} {} {} {:6s} {}'.format(idx, cmd, x, y, dict(reg)))

        if cmd == 'snd':
            stored = reg[x]
        elif cmd == 'set':
            reg[x] = val(y)
        elif cmd == 'add':
            reg[x] += val(y)
        elif cmd == 'sub':
            reg[x] -= val(y)
        elif cmd == 'mul':
            reg[x] *= val(y)
            result += 1
        elif cmd == 'mod':
            reg[x] %= val(y)
        elif cmd == 'rcv' and val(x) != 0:
            reg[x] = stored; return stored
        elif cmd == 'jnz' and val(x) != 0:
            idx += (val(y) - 1)
        elif cmd == 'jgz' and val(x) > 0:
            idx += (val(y) - 1)

        idx += 1

    return result


if __name__ == '__main__':
    # assert run(dedent("""
    # set a 1
    # add a 2
    # mul a a
    # mod a 5
    # snd a
    # set a 0
    # rcv a
    # jgz a -1
    # set a 1
    # jgz a -2
    # """).strip()) == 4

    # with open('input/d23.txt') as f:
    #     print(run(f.read().strip(), debug=True))

    asm_opt()
