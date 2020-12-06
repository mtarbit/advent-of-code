#!/usr/bin/env python


def has_dupes(arr):
    for i, a in enumerate(arr[:-1]):
        j = i + 1
        for b in arr[j:]:
            if a == b:
                return True
    return False


def run(phrase):
    phrase = phrase.split()
    return not has_dupes(phrase)


if __name__ == '__main__':
    assert run('aa bb cc dd ee') == True
    assert run('aa bb cc dd aa') == False
    assert run('aa bb cc dd aaa') == True

    with open('input/d04.txt') as f:
        num = 0
        for line in f:
            if run(line.strip()):
                num += 1
        print num
