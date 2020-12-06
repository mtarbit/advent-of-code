#!/usr/bin/env python3


def match(a, b, l):
    s = ''
    for i in range(l):
        if a[i] == b[i]:
            s += a[i]
    return s


def run(arr):
    l = len(arr[0])
    for i, a in enumerate(arr):
        for b in arr[(i + 1):]:
            s = match(a, b, l)
            if len(s) == l - 1:
                return s


if __name__ == '__main__':
    assert run("""abcde
                  fghij
                  klmno
                  pqrst
                  fguij
                  axcye
                  wvxyz""".split()) == 'fgij'

    with open('input/d02.txt', 'r') as f:
        print(run(f.read().split()))
