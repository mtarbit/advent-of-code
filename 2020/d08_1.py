#!/usr/bin/env python3

from aoc import get_lines


def run(input):
    acc = 0
    idx = 0
    idx_seen = set()

    while True:
        if idx in idx_seen:
            return acc

        idx_seen.add(idx)

        op = input[idx]
        operator, operand = op.split(' ')
        operand = int(operand)

        if operator == 'nop':
            idx += 1
        elif operator == 'acc':
            idx += 1
            acc += operand
        elif operator == 'jmp':
            idx += operand

        print(f'{idx}: {acc} ({op})')


def main():
    assert run(get_lines('d08.example')) == 5
    return run(get_lines('d08'))


if __name__ == '__main__':
    print(main())
