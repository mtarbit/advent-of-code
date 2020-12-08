#!/usr/bin/env python3

from aoc import get_lines
import re


TARGET = 'shiny gold'


def get_lookup(input):
    lookup = {}
    for line in input:
        name, contains = line.split(' bags contain ')
        if name not in lookup:
            lookup[name] = {}
        for count, sub_name in re.findall('(\d+) (.*?) bags?', contains):
            lookup[name][sub_name] = int(count)
    return lookup


def has_gold(lookup, contains):
    for name, count in contains.items():
        if name == TARGET or has_gold(lookup, lookup[name]):
            return True


def run(input):
    lookup = get_lookup(input)
    result = 0
    for name, contains in lookup.items():
        if has_gold(lookup, contains):
            result += 1
    return result


def main():
    assert run(get_lines('d07.example')) == 4
    return run(get_lines('d07'))


if __name__ == '__main__':
    print(main())
