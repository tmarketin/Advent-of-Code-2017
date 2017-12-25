from collections import defaultdict

ops = {'A': (lambda curr: (1, 1, 'B') if(curr == 0) else (0, -1, 'C')), 
       'B': (lambda curr: (1, -1, 'A') if(curr == 0) else (1, 1, 'C')),
       'C': (lambda curr: (1, 1, 'A') if(curr == 0) else (0, -1, 'D')),
       'D': (lambda curr: (1, -1, 'E') if(curr == 0) else (1, -1, 'C')),
       'E': (lambda curr: (1, 1, 'F') if(curr == 0) else (1, 1, 'A')),
       'F': (lambda curr: (1, 1, 'A') if(curr == 0) else (1, 1, 'E'))}

def part1(maxstep, state):
    tm = defaultdict(int)
    curr = 0
    for step in range(maxstep):
        wr, nextpos, nextstate = ops[state] (tm[curr])
        tm[curr] = wr
        curr = curr + nextpos
        state = nextstate

    s = 0
    for key, value in tm.items():
        s = s + value
    return s

print('Part 1: ', part1(12261543, 'A'))
