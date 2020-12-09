#!/usr/bin/env python3

from aoc import get_lines


def run_program(program):
    acc = 0
    idx = 0
    idx_seen = set()
    last_idx = len(program)

    while True:
        if idx == last_idx:
            return acc

        if idx in idx_seen:
            return False

        idx_seen.add(idx)

        cmd = program[idx]
        operator, operand = cmd.split(' ')
        operand = int(operand)

        print(f'running: {idx}, {acc} {cmd!r}')

        if operator == 'nop':
            idx += 1
        elif operator == 'acc':
            idx += 1
            acc += operand
        elif operator == 'jmp':
            idx += operand


def run(input):
    program = input.copy()
    program_change_idx = 0

    while True:
        res = run_program(program)

        if res is not False:
            return res

        print('program looped, trying modification...')

        program = input.copy()

        while True:
            cmd = program[program_change_idx]

            if cmd.startswith('nop') \
            or cmd.startswith('jmp'):
                print('modified idx:', (program_change_idx - 1))
                if cmd.startswith('nop'): cmd = cmd.replace('nop', 'jmp')
                if cmd.startswith('jmp'): cmd = cmd.replace('jmp', 'nop')
                program[program_change_idx] = cmd
                program_change_idx += 1
                break
            else:
                program_change_idx += 1


def main():
    assert run(get_lines('d08.example')) == 8
    return run(get_lines('d08'))


if __name__ == '__main__':
    print(main())
