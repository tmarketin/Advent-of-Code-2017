import copy

def load_input(fname):
    retlist = []
    with open(fname, 'r') as fp:
        for line in fp:
            retlist.append(tuple(sorted([int(x) for x in line.strip().split('/')])))
    return sorted(retlist, key = lambda tup: tup[0])

def BuildBridge(items):
    que = [[0, 0, copy.copy(items)]]
    fin = []
    while(len(que) > 0):
        end = True
        currsol = copy.deepcopy(que[0])
        del que[0]

        idx = 0
        while(idx < len(currsol[2]) and currsol[2][idx][0] <= currsol[1]):
            item = currsol[2][idx]
            if(item[0] == currsol[1]):
                newsol = [currsol[0] + item[0] + item[1], item[1], copy.copy(currsol[2])]
                newsol[2].remove(item)
                que.append(newsol)
                end = False
            if(item[1] == currsol[1] and item[0] != item[1]):
                newsol = [currsol[0] + item[0] + item[1], item[0], copy.copy(currsol[2])]
                newsol[2].remove(item)
                que.append(newsol)
                end = False
            idx = idx + 1
        if(end):
            fin.append(currsol)
    
    fin.sort(key = lambda it: it[0], reverse = True)
    return fin

items = load_input('day24.dat')
bridges = BuildBridge(items)
print('Part 1: ',bridges[0][0])

maxbridge = bridges[0]
for bridge in bridges:
    if(len(bridge[2]) < len(maxbridge[2])):
        maxbridge = bridge
print('Part 2: ', maxbridge)