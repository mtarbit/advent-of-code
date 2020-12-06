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
    max_seat_id = 0
    for s in input:
        seat_id = get_seat_id(s)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id


def main():
    assert get_seat_id('BFFFBBFRRR') == 567
    assert get_seat_id('FFFBBBFRRR') == 119
    assert get_seat_id('BBFFBBFRLL') == 820
    return run(get_lines('d05'))


if __name__ == '__main__':
    print(main())
