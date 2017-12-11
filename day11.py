from collections import Counter
from collections import defaultdict

def load_input(fname):
    with open(fname, 'r') as fp:
        s = fp.readline()
    return s.strip().split(',')

def GetDistance(d):
    ns = d['n'] - d['s']
    nesw = d['ne'] - d['sw']
    nwse = d['nw'] - d['sw']
    if(nesw*nwse > 1):
        return abs(ns) + max(abs(nesw), abs(nwse))
    else:
        return abs(ns) + abs(nesw) + abs(nwse)

def MaxDistance(inlist):
    d = defaultdict(int)
    maxdist = 0
    for item in inlist:
        d[item] = d[item] + 1
        maxdist = max(maxdist, GetDistance(d))
    return maxdist



inlist = load_input('day11.dat')
print('Part 1: ', GetDistance(Counter(inlist)))
print('Part 2: ', MaxDistance(inlist))
