from collections import defaultdict

ops = {'set': (lambda x, y: y),
       'sub': (lambda x, y: x - y),
       'mul': (lambda x, y: x*y) }

def load_instructions(fname):
    retlist = []
    with open(fname, 'r') as fp:
        for line in fp:
            retlist.append(line.strip().split())
    return retlist

def ReturnRegVal(val, regs):
    if(val in 'abcdefghijklmnopqrstuvwxyz'):
        return regs[val]
    else:
        return int(val)

def part1(inst):
    idx = 0
    regs = defaultdict(int)
    cnt = 0
    while(idx >= 0 and idx < len(inst)):
        if(inst[idx][0] == 'jnz'):
            if(ReturnRegVal(inst[idx][1], regs) != 0):
                idx = idx + ReturnRegVal(inst[idx][2], regs)
                continue
        else:
            regs[inst[idx][1]] = ops[inst[idx][0]] (ReturnRegVal(inst[idx][1], regs), ReturnRegVal(inst[idx][2], regs))
        if(inst[idx][0] == 'mul'):
            cnt = cnt + 1
        idx = idx + 1
    return cnt

def part2(inst):
    b = 99*100 + 100000
    c = b + 17000
    h = 0
    for b in range(99*100 + 100000, c + 1, 17):
        f, d = 1, 2
        for d in range(2, int(b/2)):
            if(b % d == 0):
                f = 0
        if(f == 0):
            h = h + 1
    return h

instructions = load_instructions('day23.dat')
print('Part 1: ', part1(instructions))
print('Part 2: ', part2(instructions))