#!/usr/bin/env python

from operator import xor


def sparse_hash_round(i, skip, nums, lengths):
    size = len(nums)

    for l in lengths:
        j = i + l
        k = (j % size) if j >= size else 0

        a = nums[i:j]
        b = nums[0:k]
        c = list(reversed(a + b))
        nums[i:j] = c[:len(a)]
        nums[0:k] = c[len(a):]

        i = (j + skip) % size

        skip += 1

    return i, skip, nums


def sparse_hash(lengths, rounds=64, size=256):
    i = 0
    skip = 0
    nums = list(range(size))
    lengths += [17, 31, 73, 47, 23]
    for round in range(rounds):
        i, skip, nums = sparse_hash_round(i, skip, nums, lengths)
    return nums


def dense_hash(nums, size):
    for i in range(0, len(nums), size):
        j = i + size
        yield reduce(xor, nums[i:j])


def knot_hash(s):
    lengths = map(ord, s)
    nums = sparse_hash(lengths)
    nums = dense_hash(nums, 16)
    bits = ['{:08b}'.format(n) for n in nums]
    return ''.join(bits)


def run(key, debug=False):
    n = 0
    for i in range(128):
        s = knot_hash('{}-{}'.format(key, i))
        if debug and i < 8:
            print s[:8]
        n += s.count('1')
    return n


if __name__ == '__main__':
    assert run('flqrgnkx') == 8108

    with open('input/d14.txt') as f:
        print run(f.read().strip())
