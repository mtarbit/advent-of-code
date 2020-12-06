#!/usr/bin/env python3


def run(n):
    m = (n // 3) - 2
    if m <= 0:
        return 0
    else:
        return m + run(m)


if __name__ == '__main__':
    assert run(14) == 2
    assert run(1969) == 966
    assert run(100756) == 50346

    with open('input/d01.txt', 'r') as f:
        str_list = f.read().split()
        int_list = map(int, str_list)
        res_list = map(run, int_list)
        print(sum(res_list))

