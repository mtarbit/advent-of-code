#!/usr/bin/env python


def run(s, debug=False):
    n = 0
    m = 0

    cancel = 0
    in_group = 0
    in_garbage = 0

    for c in s:
        if debug:
            print n, m, c, cancel, in_group, in_garbage

        if cancel:
            cancel = 0
            continue

        if c == '!':
            cancel = 1
        if c == '>':
            in_garbage = 0
        if not in_garbage and c == '<':
            in_garbage = 1
        if not in_garbage and c == '}':
            in_group = 0; m -= 1
        if not in_garbage and c == '{':
            in_group = 1; m += 1; n += m

    return n


if __name__ == '__main__':
    # assert is_garbage('<>')
    # assert is_garbage('<random characters>')
    # assert is_garbage('<<<<>')
    # assert is_garbage('<{!>}>')
    # assert is_garbage('<!!>')
    # assert is_garbage('<!!!>>')
    # assert is_garbage('<{o"i!a,<{i<a>')

    # assert 1 == groups('{}')
    # assert 3 == groups('{{{}}}')
    # assert 3 == groups('{{},{}}')
    # assert 6 == groups('{{{},{},{{}}}}')
    # assert 1 == groups('{<{},{},{{}}>}')
    # assert 1 == groups('{<a>,<a>,<a>,<a>}')
    # assert 5 == groups('{{<a>},{<a>},{<a>},{<a>}}')
    # assert 2 == groups('{{<!>},{<!>},{<!>},{<a>}}')

    assert 1 == run('{}')
    assert 6 == run('{{{}}}')
    assert 5 == run('{{},{}}')
    assert 16 == run('{{{},{},{{}}}}')
    assert 1 == run('{<a>,<a>,<a>,<a>}')
    assert 9 == run('{{<ab>},{<ab>},{<ab>},{<ab>}}')
    assert 9 == run('{{<!!>},{<!!>},{<!!>},{<!!>}}')
    assert 3 == run('{{<a!>},{<a!>},{<a!>},{<ab>}}')

    with open('input/d09.txt') as f:
        print run(f.read().strip(), debug=True)
