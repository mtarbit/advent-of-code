#!/usr/bin/env python


def run(s):
    banks = map(int, s.split())
    banks_seen = set()
    banks_seen_before = None
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
        elif banks_seen_before == None:
            banks_seen_before = banks[:]
            cycles = 0
        elif banks_seen_before == banks:
            return cycles


if __name__ == '__main__':
    assert run('0 2 7 0') == 4

    with open('input/d06.txt') as f:
        print run(f.read())

