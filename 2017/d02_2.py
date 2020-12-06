#!/usr/bin/env python


def get_even_quotient(nums):
    for i, n in enumerate(nums[:-1]):
        for m in nums[(i + 1):]:
            a = max(n, m)
            b = min(n, m)
            quo, rem = divmod(a, b)
            if rem == 0:
                return quo


def run(sheet):
    result = 0

    for line in sheet.strip().splitlines():
        line = line.strip().split()
        nums = map(int, line)
        result += get_even_quotient(nums)

    return result


if __name__ == '__main__':
    assert run("""
        5 9 2 8
        9 4 7 3
        3 8 6 5
    """) == 9

    with open('input/d02.txt', 'r') as f:
        print run(f.read().strip())
