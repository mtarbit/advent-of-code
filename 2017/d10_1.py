#!/usr/bin/env python


def run(n, s, debug=False):
    i = 0

    skip = 0
    numbers = list(range(n))
    lengths = map(int, s.split(','))

    for l in lengths:
        j = i + l
        k = (j % n) if j >= n else 0

        a = numbers[i:j]
        b = numbers[0:k]
        c = list(reversed(a + b))
        a = c[:len(a)]
        b = c[len(a):]

        numbers[i:j] = a
        numbers[0:k] = b

        i = (j + skip) % n

        skip += 1

        if debug:
            print "{}, {}: [{}] {}".format(l, skip, i, numbers)

    return numbers[0] * numbers[1]


if __name__ == '__main__':
    assert 12 == run(5, '3,4,1,5', debug=True)

    with open('input/d10.txt') as f:
        print run(256, f.read().strip())
