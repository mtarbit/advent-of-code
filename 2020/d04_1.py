#!/usr/bin/env python3

from aoc import get_paras


def run(input):
    n = 0

    required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    optional = set(['cid'])

    for s in input:
        fields = set()
        for part in s.split():
            k, v = part.split(':')
            fields.add(k)
        if required.issubset(fields):
            n += 1

    return n


def main():
    assert run(get_paras('d04.example')) == 2
    return run(get_paras('d04'))


if __name__ == '__main__':
    print(main())
