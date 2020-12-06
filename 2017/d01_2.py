#!/usr/bin/env python


def run(s):
    arr = map(int, s)
    tot = 0

    l = len(arr)
    for i, n in enumerate(arr):
        j = (i + (l / 2)) % l
        m = arr[j]
        if n == m:
            tot += n

    return tot


if __name__ == '__main__':
    assert run('1212') == 6
    assert run('1221') == 0
    assert run('123425') == 4
    assert run('123123') == 12
    assert run('12131415') == 4

    with open('input/d01.txt', 'r') as f:
        print run(f.read().strip())
