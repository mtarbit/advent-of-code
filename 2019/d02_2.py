#!/usr/bin/env python3


def run(memory):
    i = 0

    # print('-' * 80)

    while True:
        opcode = memory[i]
        params = memory[(i + 1):(i + 4)]

        # print(opcode, *params)

        if opcode == 99:
            break
        elif opcode == 1:
            lft, rgt, dst = params
            memory[dst] = memory[lft] + memory[rgt]
        elif opcode == 2:
            lft, rgt, dst = params
            memory[dst] = memory[lft] * memory[rgt]

        # print(memory)

        i += 4

    return memory


def chk():
    with open('input/d02.txt', 'r') as f:
        program = f.read().split(',')
        program = list(map(int, program))

        for noun in range(100):
            for verb in range(100):
                memory = program[:]
                memory[1] = noun
                memory[2] = verb
                memory = run(memory)
                output = memory[0]
                print('noun: {:2}, verb: {:2}, output: {}'.format(noun, verb, output))
                if output == 19690720:
                    return (noun, verb)


if __name__ == '__main__':
    assert run([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    assert run([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert run([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert run([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert run([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    noun, verb = chk()

    print((100 * noun) + verb)
