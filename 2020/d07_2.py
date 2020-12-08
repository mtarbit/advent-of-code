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


def bag_count(lookup, contains):
    result = 0
    for name, count in contains.items():
        result += (count + (count * bag_count(lookup, lookup[name])))
    return result


def run(input):
    lookup = get_lookup(input)
    result = bag_count(lookup, lookup[TARGET])
    return result


def main():
    assert run(get_lines('d07.example.2')) == 126
    return run(get_lines('d07'))


if __name__ == '__main__':
    print(main())
