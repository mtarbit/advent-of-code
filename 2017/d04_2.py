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
    phrase = map(sorted, phrase)
    return not has_dupes(phrase)


if __name__ == '__main__':
    assert run('abcde fghij') == True
    assert run('abcde xyz ecdab') == False
    assert run('a ab abc abd abf abj') == True
    assert run('iiii oiii ooii oooi oooo') == True
    assert run('oiii ioii iioi iiio') == False

    with open('input/d04.txt') as f:
        num = 0
        for line in f:
            if run(line.strip()):
                num += 1
        print num
