#!/usr/bin/env python3

from aoc import get_input


def run(input):
    l = len(input)
    for i in range(l - 2):
        for j in range(i + 1, l - 1):
            for k in range(j + 1, l):
                n = input[i]
                m = input[j]
                o = input[k]
                if n + m + o == 2020:
                    return n * m * o


if __name__ == '__main__':
    assert run([1721, 979, 366, 299, 675, 1456]) == 241861950
    print(run(get_input('d01', int)))
