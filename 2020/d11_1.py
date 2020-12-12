#!/usr/bin/env python3

from aoc import get_lines
import copy


def print_state(state):
    for row in state:
        print(''.join(row))
    print()


def adjacent(state, r, c):
    seats = []
    seats_position = (
        (-1, -1), (-1,  0), (-1, +1),
        ( 0, -1),           ( 0, +1),
        (+1, -1), (+1,  0), (+1, +1),
    )

    min_r, max_r = 0, len(state)
    min_c, max_c = 0, len(state[0])

    for dr, dc in seats_position:
        seat_r = r + dr
        seat_c = c + dc
        if  min_r <= seat_r < max_r \
        and min_c <= seat_c < max_c:
            seats.append(state[seat_r][seat_c])

    return seats


def occupied(state, r, c):
    return len([seat for seat in adjacent(state, r, c) if seat == '#'])


def occupied_total(state):
    n = 0
    for seat_list in state:
        for seat in seat_list:
            if seat == '#':
                n += 1
    return n


def run(input):
    input = list(map(list, input))

    curr_state = copy.deepcopy(input)
    next_state = copy.deepcopy(input)

    while True:

        curr_state = copy.deepcopy(next_state)

        for r, seat_list in enumerate(curr_state):
            for c, seat in enumerate(seat_list):
                if seat == 'L' and occupied(curr_state, r, c) == 0:
                    next_state[r][c] = '#'; continue
                if seat == '#' and occupied(curr_state, r, c) >= 4:
                    next_state[r][c] = 'L'; continue
                next_state[r][c] = curr_state[r][c]

        if curr_state == next_state:
            break

    return occupied_total(curr_state)


def main():
    assert run(get_lines('d11.example')) == 37
    return run(get_lines('d11'))


if __name__ == '__main__':
    print(main())
