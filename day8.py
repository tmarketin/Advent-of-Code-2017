from collections import defaultdict

ops = {'>': (lambda x, y: x > y),
       '<': (lambda x, y: x < y),
       '>=': (lambda x, y: x >= y),
       '<=': (lambda x, y: x <= y),
       '==': (lambda x, y: x == y),
       '!=': (lambda x, y: x != y),
       'inc': (lambda x, y: x + y),
       'dec': (lambda x, y: x - y) }

def load_instructions(fname):
    retlist = []
    with open(fname, 'r') as fp:
        for line in fp:
            retlist.append(line.strip().split())
    return retlist

def part12(instructions, regs):
    globalmax = ['', 0]
    for inst in instructions:
        if(ops[inst[5]] (regs[inst[4]], int(inst[6]))): # check condition
            regs[inst[0]] = ops[inst[1]] (regs[inst[0]], int(inst[2])) # execute instruction if true
        tmpmaxreg = max(regs.keys(), key = (lambda key: regs[key]))
        tmpmaxval = regs[tmpmaxreg]
        if(tmpmaxval > globalmax[1]):
            globalmax = [tmpmaxreg, tmpmaxval]
    retreg = max(regs.keys(), key=(lambda key: regs[key]))
    return [retreg, regs[retreg]], globalmax

instructions = load_instructions('day8.dat')
reg = defaultdict(int)
print('Part 1 and 2: ',part12(instructions, reg))
