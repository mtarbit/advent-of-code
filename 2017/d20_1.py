#!/usr/bin/env python

import re
from textwrap import dedent


def assert_equal(a, b):
    if a != b:
        raise AssertionError("{!r} is not equal to {!r}".format(a, b))


class Coord:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def from_string(s):
        return Coord(*map(int, s.split(',')))

    @property
    def manhattan_distance(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __add__(self, other):
        return Coord(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __repr__(self):
        return '<{},{},{}>'.format(self.x, self.y, self.z)


class Particle:
    def __init__(self, id, p, v, a):
        self.id = id
        self.p = Coord.from_string(p)
        self.v = Coord.from_string(v)
        self.a = Coord.from_string(a)

    def update(self):
        self.v += self.a
        self.p += self.v

    @property
    def manhattan_distance(self):
        return self.p.manhattan_distance

    def __cmp__(self, other):
        return self.manhattan_distance - other.manhattan_distance

    def __repr__(self):
        return '(id={} p={}, v={}, a={})'.format(self.id, self.p, self.v, self.a)


def run(s, debug=False):
    particles = re.findall('p=<([^>]+)>, v=<([^>]+)>, a=<([^>]+)>', s)
    particles = [Particle(id, *groups) for id, groups in enumerate(particles)]

    closest_id = None
    closest_unchanged = 0

    while True:
        for p in particles:
            p.update()

        closest = min(particles)
        if closest.id != closest_id:
            closest_id = closest.id
            closest_unchanged = 0
        else:
            closest_unchanged += 1

        if debug:
            print closest_unchanged, closest_id

        if closest_unchanged >= 300:
            break

    return closest_id


if __name__ == '__main__':
    assert_equal(run(dedent("""
    p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
    p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>
    """).strip()), 0)

    with open('input/d20.txt') as f:
        print run(f.read().strip(), debug=True)
