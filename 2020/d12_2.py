#!/usr/bin/env python3

from aoc import get_lines


def run(input):
    ship_x = 0
    ship_y = 0
    waypoint_x = 10
    waypoint_y = -1

    for line in input:
        cmd = line[0]
        num = int(line[1:])

        if cmd == 'N':
            waypoint_y -= num
        elif cmd == 'S':
            waypoint_y += num
        elif cmd == 'E':
            waypoint_x += num
        elif cmd == 'W':
            waypoint_x -= num
        elif cmd == 'R' or cmd == 'L':
            if (cmd == 'R' and num == 90) or (cmd == 'L' and num == 270):
                waypoint_x, waypoint_y = -waypoint_y, +waypoint_x
            elif (cmd == 'R' and num == 180) or (cmd == 'L' and num == 180):
                waypoint_x, waypoint_y = -waypoint_x, -waypoint_y
            elif (cmd == 'R' and num == 270) or (cmd == 'L' and num == 90):
                waypoint_x, waypoint_y = +waypoint_y, -waypoint_x
        elif cmd == 'F':
            ship_x += (waypoint_x * num)
            ship_y += (waypoint_y * num)

    return abs(ship_x) + abs(ship_y)


def main():
    assert run(get_lines('d12.example')) == 286
    return run(get_lines('d12'))


if __name__ == '__main__':
    print(main())
