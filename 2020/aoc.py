from textwrap import dedent


def get_lines(s):
    return dedent(s).strip().splitlines()


def get_paras(s):
    return dedent(s).strip().split('\n\n')


def get_input(name, map_fn=None, lines=True, paras=False):
    with open('input/{}.txt'.format(name), 'r') as f:
        input = f.read()
    if lines:
        input = input.splitlines()
    if paras:
        input = input.split('\n\n')
    if map_fn:
        input = list(map(map_fn, input))
    return input
