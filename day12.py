import re

def load_input(fname):
    retlist = []
    with open(fname, 'r') as fp:
        for line in fp:
            l = re.sub(r'[\<\-\>\,]', '', line)
            retlist.append([int(x) for x in l.strip().split()[1:]])
    return retlist

def part1(indata, startprogram):
    idx = startprogram
    res = set([idx])
    res.update(indata[idx])
    que = indata[idx]
    while(len(que) > 0):
        idx = que[0]
        que = que + [x for x in indata[idx] if x not in que and x not in res]
        res.update(indata[idx])
        que = que[1:]
    return len(res), res

def part2(indata):
    groupcount = 0
    p = set()
    idx = 0
    while(len(p) < len(indata)):
        l, g = part1(indata, idx)
        p.update(g)
        groupcount = groupcount + 1
        for a in range(len(indata)):
            if(a not in p):
                break
        idx = a
    return groupcount

indata = load_input('day12.dat')
print('Part 1: ', part1(indata, 0)[0])
print('Part 2: ', part2(indata))

