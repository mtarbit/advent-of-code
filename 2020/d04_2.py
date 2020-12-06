#!/usr/bin/env python3

from aoc import get_paras
import re


def _is_num_in_range(s, lo, hi):
    return s.isdigit() and lo <= int(s) <= hi


def byr(s):
    return _is_num_in_range(s, 1920, 2002)


def iyr(s):
    return _is_num_in_range(s, 2010, 2020)


def eyr(s):
    return _is_num_in_range(s, 2020, 2030)


def hgt(s):
    m = re.match('^(\d+)(cm|in)$', s)
    if not m: return False
    value = m.group(1)
    units = m.group(2)
    if units == 'cm':
        return _is_num_in_range(value, 150, 193)
    if units == 'in':
        return _is_num_in_range(value, 59, 76)


def hcl(s):
    return bool(re.match('^#[0-9a-f]{6}$', s))


def ecl(s):
    return bool(re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', s))


def pid(s):
    return bool(re.match('^\d{9}$', s))


def cid(s):
    return True


REQUIRED = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
OPTIONAL = set(['cid'])
REQUIRED_PLUS_OPTIONAL = REQUIRED | OPTIONAL

VALIDATORS = {
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid,
    'cid': cid,
}


def is_valid(passport):
    found = set()

    for field in passport.split():
        label, value = field.split(':')
        found.add(label)
        validator = VALIDATORS.get(label)
        if not validator:
            return False
        if not validator(value):
            return False

    return found == REQUIRED \
        or found == REQUIRED_PLUS_OPTIONAL


def run(input):
    n = 0
    for passport in input:
        if is_valid(passport):
            n += 1
    return n


def main():
    assert(byr('2002')) == True
    assert(byr('2003')) == False
    assert(hgt('60in')) == True
    assert(hgt('190cm')) == True
    assert(hgt('190in')) == False
    assert(hgt('190')) == False
    assert(hcl('#123abc')) == True
    assert(hcl('#123abz')) == False
    assert(hcl('123abc')) == False
    assert(ecl('brn')) == True
    assert(ecl('wat')) == False
    assert(pid('000000001')) == True
    assert(pid('0123456789')) == False

    assert run(get_paras('d04.example.invalid')) == 0
    assert run(get_paras('d04.example.valid')) == 4

    return run(get_paras('d04'))


if __name__ == '__main__':
    print(main())
