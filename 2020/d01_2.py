#!/usr/bin/env python3

from aoc import get_lines


def run(input):
    input = list(map(int, input))
    l = len(input)
    for i in range(l - 2):
        for j in range(i + 1, l - 1):
            for k in range(j + 1, l):
                n = input[i]
                m = input[j]
                o = input[k]
                if n + m + o == 2020:
                    return n * m * o


def main():
    assert run(get_lines('d01.example')) == 241861950
    return run(get_lines('d01'))


if __name__ == '__main__':
    print(main())
