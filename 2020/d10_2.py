#!/usr/bin/env python3

from aoc import get_lines
from functools import lru_cache


# 3 4 5 6 7
#  1 1 1 1
# 3 5 6 7
#  2 1 1
# 3 4 6 7
#  1 2 1
# 3 4 5 7
#  1 1 2
# 3 4 7
#  1 3
# 3 5 7
#  2 2
# 3 6 7
#  3 1


# 0 1 4 5 6 7 10 11 12 15 16 19 22
#  1 3 1 1 1 3  1  1  3  1  3  3

# 0 1 4 5 6 7 10 12 15 16 19 22
#  1 3 1 1 1 3  2  3  1  3  3
#               A

# 0 1 4 5 7 10 11 12 15 16 19 22
#  1 3 1 2 3  1  1  3  1  3  3
#        B

# 0 1 4 5 7 10 12 15 16 19 22
#  1 3 1 2 3  2  3  1  3  3
#        B    A

# 0 1 4 6 7 10 11 12 15 16 19 22
#  1 3 2 1 3  1  1  3  1  3  3
#      C

# 0 1 4 6 7 10 12 15 16 19 22
#  1 3 2 1 3  2  3  1  3  3
#      C      A

# 0 1 4 7 10 11 12 15 16 19 22
#  1 3 3 3  1  1  3  1  3  3
#      D

# 0 1 4 7 10 12 15 16 19 22
#  1 3 3 3  2  3  1  3  3
#      D    A

# . . = 1
#  .

# 1 1
#  2

# . . . = 3
#  . .
#   .

# 1 1 1
#  2 1
#  1 2
#   3

# . . . . = 6
#  . . .
#   . .
#    .

# 4 5 6 7 8
#  1 1 1 1
# 4 5 6   8
#   1 1 2
# 4   6 7 8
#   2 1 1
# 4 5   7 8
#   1 2 1
# 4   6   8
#    2 2
# 4     7 8
#    3 1
# 4 5     8
#    1 3


# Full disclosure: I had no idea how to do this and got tangled up trying to see some
# kind of number theory pattern in the way that the joltage difference combinations
# worked (see commented notes above). So the implementation below is basically just
# copied from Jonathan Paulson after him watching him solve the thing in seconds :/
# https://www.youtube.com/watch?v=cE88K2kFZn0


@lru_cache(maxsize=None)
def number_of_paths(input, i=0):
    if i == len(input) - 1:
        result = 1
    else:
        result = 0
        for j in range(i + 1, len(input)):
            if input[j] - input[i] <= 3:
                result += number_of_paths(input, j)
    return result


def run(input):
    input = list(map(int, input))
    input.extend([0, max(input) + 3])
    input = tuple(sorted(input))
    return number_of_paths(input)


def main():
    assert run(get_lines('d10.example.small')) == 8
    assert run(get_lines('d10.example.large')) == 19208
    return run(get_lines('d10'))


if __name__ == '__main__':
    print(main())
