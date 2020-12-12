#!/usr/bin/env python3

from aoc import get_lines


def run(input):
    x = 0
    y = 0
    d = 180

    for line in input:
        cmd = line[0]
        num = int(line[1:])

        if cmd == 'N':
            y -= num
        elif cmd == 'S':
            y += num
        elif cmd == 'E':
            x += num
        elif cmd == 'W':
            x -= num
        elif cmd == 'L':
            d = (d - num) % 360
        elif cmd == 'R':
            d = (d + num) % 360
        elif cmd == 'F':
            if d == 180:
                x += num
            elif d == 0:
                x -= num
            elif d == 90:
                y -= num
            elif d == 270:
                y += num

    return x + y


def main():
    assert run(get_lines('d12.example')) == 25
    return run(get_lines('d12'))


if __name__ == '__main__':
    print(main())
