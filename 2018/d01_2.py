#!/usr/bin/env python3


def run(arr):
    arr = list(map(int, arr))
    tot = 0
    tot_seen = set([tot])

    while True:
        for num in arr:
            tot += num
            if tot in tot_seen:
                return tot
            tot_seen.add(tot)


if __name__ == '__main__':
    assert run(['+1', '-1']) == 0
    assert run(['+3', '+3', '+4', '-2', '-4']) == 10
    assert run(['-6', '+3', '+8', '+5', '-6']) == 5
    assert run(['+7', '+7', '-2', '-7', '-4']) == 14

    with open('input/d01.txt', 'r') as f:
        print(run(f.read().split()))
