#!/usr/bin/env python


def run(a_start, b_start, pairs=5000000, debug=False):
    def gen_factory(val, fac, mul):
        def gen(val):
            while True:
                val *= fac
                val %= 2147483647
                if not val % mul:
                    yield val
        return gen(val)

    gen_a = gen_factory(a_start, 16807, 4)
    gen_b = gen_factory(b_start, 48271, 8)

    lower_16 = lambda n: '{:032b}'.format(n)[-16:]

    n = 0
    for i in range(pairs):
        a = lower_16(next(gen_a))
        b = lower_16(next(gen_b))
        if debug and not i % 1000000:
            print i
        if a == b:
            n += 1

    return n


if __name__ == '__main__':
    assert run(65, 8921, pairs=1056) == 1
    assert run(65, 8921, debug=True) == 309

    with open('input/d15.txt') as f:
        print run(*map(int, f.read().split()))
