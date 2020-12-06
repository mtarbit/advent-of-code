#!/usr/bin/env python


def run(s, debug=False):
    n = 0
    m = 0

    cancel = 0
    junked = 0
    in_group = 0
    in_garbage = 0

    for c in s:
        if debug:
            print junked, m, c, cancel, in_group, in_garbage

        if in_garbage:
            if cancel:
                cancel = 0; continue
            elif c == '!':
                cancel = 1
            elif c == '>':
                in_garbage = 0
            else:
                junked += 1
        else:
            if c == '<':
                in_garbage = 1
            elif c == '}':
                in_group = 0; m -= 1
            elif c == '{':
                in_group = 1; m += 1; n += m

    return junked


if __name__ == '__main__':
    assert 0 == run('<>')
    assert 17 == run('<random characters>')
    assert 3 == run('<<<<>')
    assert 2 == run('<{!>}>')
    assert 0 == run('<!!>')
    assert 0 == run('<!!!>>')
    assert 10 == run('<{o"i!a,<{i<a>')

    with open('input/d09.txt') as f:
        print run(f.read().strip(), debug=True)
