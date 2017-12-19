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

def ReturnRegVal(val, regs):
    if(val in 'abcdefghijklmnopqrstuvwxyz'):
        return regs[val]
    else:
        return int(val)

def Simulate_part1(instructions):
    inst_pointer = 0
    reg = defaultdict(int)
    while(inst_pointer < len(instructions) and inst_pointer >= 0):
        if(instructions[inst_pointer][0] == 'snd'):
            reg['last'] = ReturnRegVal(instructions[inst_pointer][1], reg)
        
        if(instructions[inst_pointer][0] == 'set'):
            reg[instructions[inst_pointer][1]] = ReturnRegVal(instructions[inst_pointer][2], reg)

        if(instructions[inst_pointer][0] == 'add'):
            reg[instructions[inst_pointer][1]] = reg[instructions[inst_pointer][1]] + ReturnRegVal(instructions[inst_pointer][2], reg)
        
        if(instructions[inst_pointer][0] == 'mul'):
            reg[instructions[inst_pointer][1]] = reg[instructions[inst_pointer][1]]*ReturnRegVal(instructions[inst_pointer][2], reg)

        if(instructions[inst_pointer][0] == 'mod'):
            reg[instructions[inst_pointer][1]] = reg[instructions[inst_pointer][1]] % ReturnRegVal(instructions[inst_pointer][2], reg)

        if(instructions[inst_pointer][0] == 'rcv'):
            if(reg[instructions[inst_pointer][1]] != 0):
                return reg['last']
        
        if(instructions[inst_pointer][0] == 'jgz'):
            if(reg[instructions[inst_pointer][1]] > 0):
                inst_pointer = inst_pointer + ReturnRegVal(instructions[inst_pointer][2], reg)
                continue

        inst_pointer = inst_pointer + 1

def Simulate_part2(instructions):
    inst_pointer = [0, 0]
    reg = [defaultdict(int), defaultdict(int)]
    reg[0]['p'] = 0
    reg[1]['p'] = 1
    status = ['running', 'running']
    runningID = 0
    otherID = 1
    send_counter = [0, 0]
    send_queue = [[], []]
    iter_count = -1
    while(status[0] != 'finished' and status[1] != 'finished'):
        iter_count = iter_count + 1
        comm = instructions[inst_pointer[runningID]][0]
        reg1 = instructions[inst_pointer[runningID]][1]
        if(len(instructions[inst_pointer[runningID]]) > 2):
            reg2 = ReturnRegVal(instructions[inst_pointer[runningID]][2], reg[runningID])

        if(comm == 'snd'):
            send_queue[runningID].append(ReturnRegVal(reg1, reg[runningID]))
            send_counter[runningID] = send_counter[runningID] + 1
        
        if(comm == 'set'):
            reg[runningID][reg1] = reg2

        if(comm == 'add'):
            reg[runningID][reg1] = reg[runningID][reg1] + reg2
        
        if(comm == 'mul'):
            reg[runningID][reg1] = reg[runningID][reg1]*reg2

        if(comm == 'mod'):
            reg[runningID][reg1] = reg[runningID][reg1] % reg2

        if(comm == 'rcv'):
            if(len(send_queue[otherID]) > 0):
                reg[runningID][reg1] = send_queue[otherID][0]
                send_queue[otherID] = send_queue[otherID][1:]
                status[runningID] = 'running'
                inst_pointer[runningID] = inst_pointer[runningID] + 1
                continue
            
            status[runningID] = 'waiting' 
            if(status[runningID] == 'waiting' and status[otherID] == 'waiting' and len(send_queue[0]) == 0 and len(send_queue[1]) == 0):
                return iter_count, send_counter # if deadlock

            if(status[runningID] == 'waiting' and status[otherID] == 'finished'):
                return iter_count, send_counter

            tmp = runningID
            runningID = otherID
            otherID = tmp
            continue    

        if(comm == 'jgz'):
            if(reg[runningID][reg1] > 0 or reg1 == '1'):
                inst_pointer[runningID] = inst_pointer[runningID] + reg2
                continue

        inst_pointer[runningID] = inst_pointer[runningID] + 1
        if(inst_pointer[runningID] > len(instructions)):
            status[runningID] = 'finished'
            if(status[otherID] == 'finished'):
                return iter_count, send_counter
            runningID = otherID

instructions = load_instructions('day18.dat')
print('Part 1: ', Simulate_part1(instructions))
print('Part 2: ', Simulate_part2(instructions))
