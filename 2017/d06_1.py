#!/usr/bin/env python


def run(s):
    banks = map(int, s.split())
    banks_seen = set()
    cycles = 0

    while True:
        cycles += 1

        i = banks.index(max(banks))
        n = banks[i]
        banks[i] = 0
        for _ in range(n):
            i += 1
            i %= len(banks)
            banks[i] += 1

        if repr(banks) not in banks_seen:
            banks_seen.add(repr(banks))
        else:
            return cycles


if __name__ == '__main__':
    assert run('0 2 7 0') == 5

    with open('input/d06.txt') as f:
        print run(f.read())
