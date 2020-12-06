#!/usr/bin/env python3


def count(val):
    d = {}

    has_2 = 0
    has_3 = 0

    for c in val:
        if c not in d:
            d[c] = 0
        d[c] += 1

    for n in d.values():
        if n == 2: has_2 += 1
        if n == 3: has_3 += 1

    return (has_2, has_3)


def check(arr):
    has_2_count = 0
    has_3_count = 0

    for val in arr:
        has_2, has_3 = count(val)
        if has_2: has_2_count += 1
        if has_3: has_3_count += 1

    return has_2_count * has_3_count


if __name__ == '__main__':
    samples = """
    abcdef
    bababc
    abbcde
    abcccd
    aabcdd
    abcdee
    ababab
    """.split()

    assert count(samples[0]) == (0, 0)
    assert count(samples[1]) == (1, 1)
    assert count(samples[2]) == (1, 0)
    assert count(samples[3]) == (0, 1)
    assert count(samples[4]) == (2, 0)
    assert count(samples[5]) == (1, 0)
    assert count(samples[6]) == (0, 2)
    assert check(samples) == 12

    with open('input/d02.txt', 'r') as f:
        print(check(f.read().split()))
