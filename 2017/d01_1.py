#!/usr/bin/env python


def run(s):
    arr = map(int, s)
    tot = 0
    for i, n in enumerate(arr):
        j = (i + 1) % len(arr)
        m = arr[j]
        if n == m:
            tot += n
    return tot


if __name__ == '__main__':
    assert run('1122') == 3
    assert run('1111') == 4
    assert run('1234') == 0
    assert run('91212129') == 9

    with open('input/d01.txt', 'r') as f:
        print run(f.read().strip())
