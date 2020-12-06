#!/usr/bin/env python


def run(s):
    idx = 0
    arr = map(int, s.split())
    res = 0
    while True:
        try:
            val = arr[idx]
        except IndexError:
            return res
        else:
            arr[idx] = val + 1
            idx += val
            res += 1


if __name__ == '__main__':
    assert run('0 3 0 1 -3') == 5

    with open('input/d05.txt') as f:
        print run(f.read())
