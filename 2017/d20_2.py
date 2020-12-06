#!/usr/bin/env python

import re
from collections import defaultdict
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

    def as_tuple(self):
        return (self.x, self.y, self.z)

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
    def distance(self):
        return sum(map(abs, self.p.as_tuple()))

    def __cmp__(self, other):
        return self.distance - other.distance

    def __repr__(self):
        return '(id={} p={}, v={}, a={})'.format(self.id, self.p, self.v, self.a)


def run(s, debug=False):
    particles = re.findall('^p=<([^>]+)>, v=<([^>]+)>, a=<([^>]+)>$', s, re.M)
    particles = [Particle(id, *groups) for id, groups in enumerate(particles)]

    remaining = None
    remaining_unchanged = 0

    while True:

        if debug:
            print remaining_unchanged, remaining

        positions = defaultdict(list)
        survivors = []

        for i, p in enumerate(particles):
            p.update()
            positions[p.p.as_tuple()].append(i)

        for k, v in positions.items():
            if len(v) == 1:
                survivors.append(particles[v[0]])

        particles = survivors
        particles_len = len(particles)

        if remaining != particles_len:
            remaining = particles_len
        else:
            remaining_unchanged += 1

        if remaining_unchanged > 250:
            break

    return remaining


if __name__ == '__main__':
    assert_equal(run(dedent("""
    p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>
    p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
    p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
    p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>
    """).strip()), 1)

    with open('input/d20.txt') as f:
        print run(f.read().strip(), debug=True)
