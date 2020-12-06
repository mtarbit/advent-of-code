#!/usr/bin/env python3

from aoc import get_lines


def get_seat_id(s):
    b = ''
    for c in s:
        if c == 'B' \
        or c == 'R':
            b += '1'
        else:
            b += '0'
    return int(b, 2)


def run(input):
    seat_id_list = []
    for s in input:
        seat_id_list.append(get_seat_id(s))
    seat_id_list.sort()

    for i in range(len(seat_id_list)):
        curr = seat_id_list[i]
        next = seat_id_list[i + 1]
        if next != curr + 1:
            return curr + 1


def main():
    assert get_seat_id('BFFFBBFRRR') == 567
    assert get_seat_id('FFFBBBFRRR') == 119
    assert get_seat_id('BBFFBBFRLL') == 820
    return run(get_lines('d05'))


if __name__ == '__main__':
    print(main())
