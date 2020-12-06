def get_lines(name):
    return get_input(name).splitlines()

def get_paras(name):
    return get_input(name).split('\n\n')

def get_input(name):
    with open('input/{}'.format(name), 'r') as f:
        input = f.read()
    return input
