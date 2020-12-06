#!/usr/bin/env python3


def run(program):
    i = 0

    # print('-' * 80)

    while True:
        opcode = program[i]
        params = program[(i + 1):(i + 4)]

        # print(opcode, *params)

        if opcode == 99:
            break
        elif opcode == 1:
            lft, rgt, dst = params
            program[dst] = program[lft] + program[rgt]
        elif opcode == 2:
            lft, rgt, dst = params
            program[dst] = program[lft] * program[rgt]

        # print(program)

        i += 4

    return program


if __name__ == '__main__':
    assert run([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    assert run([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert run([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert run([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert run([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    with open('input/d02.txt', 'r') as f:
        program = f.read().split(',')
        program = list(map(int, program))

        program[1] = 12
        program[2] = 2

        program = run(program)

        print(program[0])
