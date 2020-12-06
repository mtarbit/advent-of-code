#!/usr/bin/env python




def run(n, debug=False):
    arr = [0]
    idx = 0

    for val in xrange(2017):
        val += 1
        idx += n
        idx %= len(arr)
        idx += 1
        arr.insert(idx, val)

    return arr[idx + 1]


if __name__ == '__main__':
    assert run(3) == 638

    with open('input/d17.txt') as f:
        print run(int(f.read().strip()))
