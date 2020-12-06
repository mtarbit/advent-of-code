#!/usr/bin/env python3


def run(s):
    arr = list(map(int, s.split()))
    tot = sum(arr)
    return tot


if __name__ == '__main__':
    assert run('+1\n+1\n+1') == 3
    assert run('+1\n+1\n-2') == 0
    assert run('-1\n-2\n-3') == -6

    with open('input/d01.txt', 'r') as f:
        print(run(f.read()))
