ops = {'d': lambda r, c: (r + 1, c),
       'u': lambda r, c: (r - 1, c),
       'l': lambda r, c: (r, c - 1),
       'r': lambda r, c: (r, c + 1) }

def load_input(fname):
    retlist = []
    with open(fname, 'r') as fp:
        for line in fp:
            retlist.append(line.strip('\n'))
    return retlist

def FollowPath(pmap, row, col, d):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pp = []
    row, col = ops[d] (row, col)
    step = 1
    while(pmap[row][col] not in '+ '):
        if(pmap[row][col] in letters):
            pp.append(pmap[row][col])
        row, col = ops[d] (row, col)
        step = step + 1
    
    if(pmap[row][col] == ' '): # end
        d = 'x'
        step = step - 1
        return pp, row, col, d, step

    if(d == 'd' or d == 'u'): # check left and right
        if(col > 0 and pmap[row][col - 1] in ('-' + letters)):
            d = 'l'
        elif(col < len(pmap[0]) - 1 and pmap[row][col + 1] in ('-' + letters)):
            d = 'r'
    elif(d == 'l' or d == 'r'): # check up and down
        if(row > 0 and pmap[row - 1][col] in ('|' + letters)):
            d = 'u'
        elif(row < len(pmap) - 1 and pmap[row + 1][col] in ('|' + letters)):
            d = 'd'
    
    return pp, row, col, d, step

def part12(pmap):
    step = 1
    path = []
    row = 0
    col = pmap[row].index('|')
    direction = 'd'
    done = False
    while(not done):
        auxpath, row, col, direction, auxstep = FollowPath(pmap, row, col, direction)
        if(direction == 'x'):
            done = True
        path = path + auxpath
        step = step + auxstep
    return ''.join(path), step

def CheckLetters(pmap):
    s = []
    for row in pmap:
        for col in row:
            if(col in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                s.append(col)
    return ''.join(s)

input_map = load_input('day19.dat')
print('Part 1 and 2: ', part12(input_map))
