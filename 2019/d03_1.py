#!/usr/bin/env python3



def get_points(wire):
    points = []

    x = 0
    y = 0

    for move in wire:
        c = move[0]
        n = int(move[1:])

        for _ in range(n):

            if c == 'U':
                y += 1
            elif c == 'D':
                y -= 1
            elif c == 'L':
                x -= 1
            elif c == 'R':
                x += 1

            points.append((x, y))

    return points


def run(s):
    a, b = [x.split(',') for x in s.split()]

    a_points = get_points(a)
    b_points = get_points(b)
    x_points = set(a_points) & set(b_points)
    x_points_distances = [(abs(x) + abs(y)) for x, y in x_points]

    return min(x_points_distances)


if __name__ == '__main__':
    assert run('R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83') == 159
    assert run('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7') == 135

    with open('input/d03.txt', 'r') as f:
        print(run(f.read()))
