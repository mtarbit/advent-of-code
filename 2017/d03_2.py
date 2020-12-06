#!/usr/bin/env python

import math


# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806  ...  ...


#     r  c
#     -  -
#  1:  0  0  *  r: 0, c: 1
#  2:  0  1  *  r:-1, c: 0
#  3: -1  1  *  r: 0, c:-1
#  _: -1  0
#  5: -1 -1  *  r: 1, c: 0
#  _:  0 -1
#  7:  1 -1  *  r: 0, c: 1
#  _:  1  0
#  _:  1  1
# 10:  1  2  *  r:-1, c: 0
# __:  0  2
# __: -1  2
# 13: -2  2  *  r: 0, c:-1
# __: -2  1
# __: -2  0
# __: -2 -1
# 17: -2 -2  *  r: 1, c: 0
# __: -1 -2
# __:  0 -2
# __:  1 -2
# 21:  2 -2  *  r: 0, c: 1
# __:  2 -1
# __:  2  0


def adjacent(r, c):
    return (
        (r - 1, c - 1),
        (r - 1, c    ),
        (r - 1, c + 1),
        (r    , c - 1),
        (r    , c + 1),
        (r + 1, c - 1),
        (r + 1, c    ),
        (r + 1, c + 1),
    )


def run(n):
    spiral = {}
    corner_idx = []
    corner_inc = ((0,1), (-1,0), (0,-1), (1,0))

    r, c = 0, 0

    r_inc = 0
    c_inc = 0

    i = 1

    while i:
        summed = sum(spiral.get(a, 0) for a in adjacent(r, c))
        result = summed or 1
        spiral[(r,c)] = result

        if result > n:
            break

        # The corners of the spiral have indexes which
        # follow a "quarter squares plus one" series.
        # See: https://oeis.org/A033638
        corner_idx.append(int(math.floor((i ** 2) / 4) + 1))

        try:
            # At each corner we change the increment
            # values for our row and column numbers:
            r_inc, c_inc = corner_inc[corner_idx.index(i) % 4]
        except ValueError:
            pass

        r += r_inc
        c += c_inc
        i += 1

    return result


if __name__ == '__main__':
    print run(312051)
