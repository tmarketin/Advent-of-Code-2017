import copy 

def load_input(fname):
    retval = []
    with open(fname, 'r') as fp:
        for line in fp:
            retval.append([int(x) for x in line.strip().split(':')])
    return retval

def SingleScannerTick(scanner):
    if(scanner[1] == 'd'):
        if(scanner[0] < scanner[2] - 1):
            scanner[0] = scanner[0] + 1
        else:
            scanner[0] = scanner[0] - 1
            scanner[1] = 'u'
    else:
        if(scanner[0] > 0):
            scanner[0] = scanner[0] - 1
        else:
            scanner[0] = scanner[0] + 1
            scanner[1] = 'd'
    return

def AllScannersTick(scanners):
    for s in scanners:
        if(s[0] >= 0): # has scanner
            SingleScannerTick(s)
    return

def GenerateScanners(layers):
    final_layer = layers[len(layers) - 1][0]
    scanners = [[-1, 'd'] for x in range(final_layer + 1)]
    for l in layers:
        scanners[l[0]][0] = 0
        scanners[l[0]].append(l[1])
    return scanners

def part1(layers, scanners):
    final_layer = layers[len(layers) - 1][0]

    severity = -1
    pos = -1
    while(pos < final_layer):
        # move player
        pos = pos + 1
        if(scanners[pos][0] == 0): # collision
            if(severity == -1):
                severity = 0
            severity = severity + pos*scanners[pos][2]
        # tick scanners
        AllScannersTick(scanners)
    return severity

def part2(layers):
    tick = -1
    chk = True
    while(chk):
        tick = tick + 1
        chk = False
        for l in layers:
            if((tick + l[0]) % (2*l[1] - 2) == 0):
                chk = True
    return tick


layers = load_input('day13.dat')
print('Part 1: ', part1(layers, GenerateScanners(layers)))
print('Part 2: ', part2(layers))
