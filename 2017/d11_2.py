#!/usr/bin/env python

from math import ceil

#           + --- +
#          /   |   \
#   + --- + ------- + --- +
#  /   |   \   |   /   |   \
# + ------- + --- + ------- +
#  \   |   /   |   \   |   /
#   + --- + ------- + --- +
#  /   |   \   |   /   |   \
# + ------- + --- + ------- +
#  \   |   /   |   \   |   /
#   + --- + ------- + --- +
#          \   |   /
#           + --- +


def run(s):
    dirs = {'n': 0.0, 'e': 0.0, 'w': 0.0, 's': 0.0}
    opps = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    steps = 0
    steps_max = 0

    for dir in s.split(','):
        if len(dir) == 1:
            dirs[dir] += 1
        else:
            ns = dir[0]
            ew = dir[1]

            if dirs.get(opps[ns]) > 0:
                dirs[opps[ns]] -= 0.5
            else:
                dirs[ns] += 0.5

            if dirs.get(opps[ew]) > 0:
                dirs[opps[ew]] -= 1
            else:
                dirs[ew] += 1

        steps = int(ceil(max(dirs.values())))

        if steps > steps_max:
            steps_max = steps

    return steps_max


if __name__ == '__main__':
    # assert run('ne,ne,ne') == 3
    # assert run('ne,ne,sw,sw') == 0
    # assert run('ne,ne,s,s') == 2
    # assert run('se,sw,se,sw,sw') == 3

    with open('input/d11.txt') as f:
        print run(f.read().strip())
