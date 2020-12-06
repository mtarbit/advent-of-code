#!/usr/bin/env python


def run(n, debug=False):
    idx = 0

    val_one = 0
    for val in xrange(5 * 10 ** 7):
        val += 1
        idx += n
        idx %= val
        idx += 1
        if idx == 1:
            val_one = val
            if debug:
                print val_one

    return val_one


if __name__ == '__main__':
    with open('input/d17.txt') as f:
        print run(int(f.read().strip()), debug=True)
