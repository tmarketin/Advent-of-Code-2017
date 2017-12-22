from collections import defaultdict
import copy

ops = {'d': lambda x, y: (x, y - 1),
       'u': lambda x, y: (x, y + 1),
       'l': lambda x, y: (x - 1, y),
       'r': lambda x, y: (x + 1, y) }
       
def load_input(fname):
    retlist = []
    auxlist = []
    with open(fname, 'r') as fp:
        for line in fp:
            auxlist.append([x for x in line.strip()])
    dim = int((len(auxlist) - 1)/2)
    for row in range(len(auxlist)):
        for col in range(len(auxlist)):
            if(auxlist[row][col] == '#'):
                retlist.append((col - dim, dim - row))
    return retlist

dirs = ['u', 'r', 'd', 'l']
def ChangeDir(currdir, lr):
    if(lr == 'r'):
        idx = (dirs.index(currdir) + 1) % len(dirs)
    if(lr == 'l'):
        idx = dirs.index(currdir) - 1
    return dirs[idx]

def ReverseDir(currdir):
    return dirs[(dirs.index(currdir) + 2) % len(dirs)]

def part1(infected, maxiter):
    cnt = 0
    x = 0
    y = 0
    d = 'u'
    for iter in range(maxiter):
        if((x, y) in infected):
            d = ChangeDir(d, 'r')
            infected.remove((x,y))
        else:
            d = ChangeDir(d, 'l')
            infected.append((x, y))
            cnt = cnt + 1
        x, y = ops[d] (x, y)
    return cnt

def part2(infected, maxiter):
    cnt = 0
    grid = defaultdict(lambda: '.')
    for item in infected:
        grid[item] = 'I'
    pos = (0, 0)
    d = 'u'
    for iter in range(maxiter):
        if(grid[pos] == 'F'):
            d = dirs[(dirs.index(d) + 2) % 4]
            del grid[pos]
        elif(grid[pos] == 'I'):
            d = dirs[(dirs.index(d) + 1) % 4]
            grid[pos] = 'F'
        elif(grid[pos] == 'W'):
            grid[pos] = 'I'
            cnt = cnt + 1
        else:
            d = dirs[dirs.index(d) - 1]
            grid[pos] = 'W'
        
        pos = ops[d] (pos[0], pos[1])
    return cnt

infected = load_input('day22.dat')
print('Part 1: ', part1(copy.copy(infected), 10000))
print('Part 2: ', part2(infected, 10000000))
