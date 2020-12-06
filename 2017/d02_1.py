#!/usr/bin/env python


def run(sheet):
    result = 0

    for line in sheet.strip().splitlines():
        line = line.strip().split()
        nums = map(int, line)
        result += max(nums) - min(nums)

    return result


if __name__ == '__main__':
    assert run("""
        5 1 9 5
        7 5 3
        2 4 6 8
    """) == 18

    with open('input/d02.txt', 'r') as f:
        print run(f.read().strip())
