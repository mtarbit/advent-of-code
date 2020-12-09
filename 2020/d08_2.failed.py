#!/usr/bin/env python3

from aoc import get_lines


def run(input):
    program = input.copy()

    print(program)

    acc = 0
    idx = 0

    idx_modifications_tried = set()
    idx_states = []
    acc_states = []

    last_idx = len(program)

    while True:

        if idx == last_idx:
            return acc

        if idx in idx_states:
            # About to loop so try rewinding to an earlier state and
            # resuming with a modified version of the program instead.
            program = input.copy()

            print('=' * 80)
            print(f'detected loop at index {idx}, rewinding...')
            print('idx states:', idx_states)
            print('acc states:', acc_states)
            print('-' * 80)

            while True:
                idx = idx_states.pop()
                acc = acc_states.pop()
                cmd = program[idx]

                print(f'popped: {idx}, {acc}, {cmd!r}')

                if cmd.startswith('nop') \
                or cmd.startswith('jmp'):
                    if idx in idx_modifications_tried:
                        continue
                    else:
                        idx_modifications_tried.add(idx)

                    if cmd.startswith('nop'): cmd = cmd.replace('nop', 'jmp')
                    if cmd.startswith('jmp'): cmd = cmd.replace('jmp', 'nop')

                    program[idx] = cmd

                    print('~' * 80)
                    print('trying modified program...')
                    print(program)

                    break

        idx_states.append(idx)
        acc_states.append(acc)

        try:
            cmd = program[idx]
        except:
            print('errored at index:', idx)
            print('err with program:', program)
            raise

        print(f'running: {idx}, {acc}, {cmd!r}')

        operator, operand = cmd.split(' ')
        operand = int(operand)

        if operator == 'nop':
            idx += 1
        elif operator == 'acc':
            idx += 1
            acc += operand
        elif operator == 'jmp':
            idx += operand


def main():
    assert run(get_lines('d08.example')) == 8
    return run(get_lines('d08'))


if __name__ == '__main__':
    print(main())
