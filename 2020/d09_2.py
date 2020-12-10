#!/usr/bin/env python3

from aoc import get_lines


def run(input, target):
    input = list(map(int, input))

    l = len(input)

    for i in range(l - 1):
        for j in range((i + 2), l):
            a = input[i:j]
            n = sum(a)
            if n == target:
                return min(a) + max(a)
            elif n > target:
                break


def main():
    assert run(get_lines('d09.example'), 127) == 62
    return run(get_lines('d09'), 57195069)


if __name__ == '__main__':
    print(main())
