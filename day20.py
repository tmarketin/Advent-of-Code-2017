import re
import numpy as np

def load_input(fname):
    retlist = []
    cnt = 0
    with open(fname, 'r') as fp:
        for line in fp:
            l = re.sub(r'[\<\>pva=]', '', line)
            vals = [int(x) for x in l.strip().split(',')]
            retlist.append({'r': np.asarray(vals[0:3]), 'v': np.asarray(vals[3:6]), 'a': np.asarray(vals[6:]), 'dist': abs(vals[0]) + abs(vals[1]) + abs(vals[2]), 'idx': cnt})
            cnt = cnt + 1
    return retlist

def part1(pos):
    sol = 0
    mina = sum(abs(pos[0]['a']))
    for partnum in range(1, len(pos)):
        if(sum(abs(pos[partnum]['a'])) < mina):
            sol = partnum
            mina = sum(abs(pos[partnum]['a']))
    return sol, pos[sol]

def SimulateStep(pos):
    for part in pos:
        part['v'] = part['v'] + part['a']
        part['r'] = part['r'] + part['v']
        part['dist'] = sum(abs(part['r']))
    return

def EliminateCollisions(pos):
    delidx = []
    for l1 in range(len(pos) - 1):
        for l2 in range(l1 + 1, len(pos)):
            if(pos[l1]['dist'] == pos[l2]['dist']): # possibly identical
                if(np.array_equal(pos[l1]['r'],pos[l2]['r'])):
                    if(l1 not in delidx):
                        delidx.append(l1)
                    if(l2 not in delidx):
                        delidx.append(l2)
    delidx.sort(reverse = True)
    if(len(delidx) > 0):
        print(delidx)
        for idx in delidx:
            del pos[idx]
    return


def part2(pos, maxsteps):
    count = 0
    while(count < maxsteps):
        SimulateStep(pos)
        EliminateCollisions(pos)
        count = count + 1
    return len(pos)

init_pos = load_input('day20.dat')
print('Part 1: ', part1(init_pos))
print('Part 2: ', part2(init_pos, 100))
