#!/usr/bin/env python3

from aoc import get_paras, get_input
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


if __name__ == '__main__':
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

    assert run(get_paras('''
        eyr:1972 cid:100
        hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

        iyr:2019
        hcl:#602927 eyr:1967 hgt:170cm
        ecl:grn pid:012533040 byr:1946

        hcl:dab227 iyr:2012
        ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

        hgt:59cm ecl:zzz
        eyr:2038 hcl:74454a iyr:2023
        pid:3556412378 byr:2007
    ''')) == 0

    assert run(get_paras('''
        pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f

        eyr:2029 ecl:blu cid:129 byr:1989
        iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

        hcl:#888785
        hgt:164cm byr:2001 iyr:2015 cid:88
        pid:545766238 ecl:hzl
        eyr:2022

        iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
    ''')) == 4

    print(run(get_input('d04', lines=False, paras=True)))
