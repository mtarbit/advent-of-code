#!/usr/bin/env python3


def run(s):
    run_length = 1
    has_double = False

    # print('-' * 80)

    for i in range(1, len(s)):
        prev = int(s[i - 1])
        curr = int(s[i])
        if prev > curr:
            return False
        if prev == curr:
            run_length += 1
        else:
            if run_length == 2:
                has_double = True
            run_length = 1

        # print(prev, curr, ':', run_length, has_double)

    if run_length == 2:
        has_double = True

    return has_double


if __name__ == '__main__':
    assert run('112233') == True
    assert run('123444') == False
    assert run('111122') == True

    count = 0
    for n in range(134564, 585159):
        s = str(n)
        if run(s):
            count += 1

    print(count)
