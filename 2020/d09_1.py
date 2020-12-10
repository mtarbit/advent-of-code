#!/usr/bin/env python3

from aoc import get_lines


def is_summed_pair(x, arr):
    l = len(arr)
    for i in range(l - 1):
        for j in range((i + 1), l):
            n = arr[i]
            m = arr[j]
            if x == (n + m):
                return True
    return False


def run(input, preamble):
    input = list(map(int, input))

    for i in range(len(input) - preamble):
        j = i + preamble
        n = input[j]
        if not is_summed_pair(n, input[i:j]):
            return n


def main():
    assert run(get_lines('d09.example'), 5) == 127
    return run(get_lines('d09'), 25)


if __name__ == '__main__':
    print(main())
