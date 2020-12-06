#!/usr/bin/env python

from operator import xor


def knot_hash(i, skip, nums, lengths):
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
        i, skip, nums = knot_hash(i, skip, nums, lengths)
    return nums


def dense_hash(nums, size):
    for i in range(0, len(nums), size):
        j = i + size
        yield reduce(xor, nums[i:j])


def run(s):
    lengths = map(ord, s)
    nums = sparse_hash(lengths)
    nums = dense_hash(nums, 16)
    hexs = ['{:02x}'.format(n) for n in nums]
    return ''.join(hexs)


if __name__ == '__main__':
    assert knot_hash(0, 0, [0, 1, 2, 3, 4], [3, 4, 1, 5]) == (4, 4, [3, 4, 2, 1, 0])
    assert next(dense_hash([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22], 16)) == 64
    assert run('') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert run('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert run('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert run('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

    with open('input/d10.txt') as f:
        print run(f.read().strip())
